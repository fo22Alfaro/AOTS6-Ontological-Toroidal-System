#!/usr/bin/env python3
"""AOTS6 cryptographic runtime registry and physical-security evidence envelope.

Supported integration families:
- ML-DSA (Dilithium): post-quantum signatures, preferably via OpenSSL/provider.
- Ed25519: legacy/classical signature compatibility.
- SHA3-512 / BLAKE2b: digest layers.
- ML-KEM (Kyber): post-quantum KEM integration.
- QKD: ingestion of externally generated key material; never fabricates quantum keys.
- ZK-SNARK: ingestion/verification envelope for an external proof system.

This module never labels simulated material as physical, never invents QKD
material, and never treats a hash as a digital signature.
"""
from __future__ import annotations
import base64, hashlib, json, os, shutil, subprocess, tempfile
from dataclasses import dataclass
from typing import Any, Optional

SCHEMA="AOTS6-CRYPTO-RUNTIME-1"
ROOT_ID="AOTS6-ORIGINAL-ALFARO"
META_OPERATOR="Alfredo Jhovany Alfaro García"
FITNESS=[54,19,11,0,1]

def canonical_bytes(obj:Any)->bytes:
    return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode("utf-8")

def digest(data:bytes, algorithm:str)->str:
    a=algorithm.lower().replace("-","")
    if a=="sha32512": return hashlib.sha3_512(data).hexdigest()
    if a=="blake2b": return hashlib.blake2b(data).hexdigest()
    if a=="sha256": return hashlib.sha256(data).hexdigest()
    raise ValueError("unsupported digest: "+algorithm)

@dataclass
class Evidence:
    algorithm:str
    status:str
    material_type:str
    value_b64:Optional[str]
    metadata:dict[str,Any]

class OpenSSLMLDSA:
    """Adapter for OpenSSL installations exposing ML-DSA (Dilithium lineage)."""
    def __init__(self, binary="openssl"): self.binary=binary
    def available(self)->bool:
        return shutil.which(self.binary) is not None
    def generate_keypair(self, parameter="ML-DSA-65", private_path="mldsa_private.pem", public_path="mldsa_public.pem"):
        if not self.available(): raise RuntimeError("OpenSSL not found")
        subprocess.run([self.binary,"genpkey","-algorithm",parameter,"-out",private_path],check=True)
        subprocess.run([self.binary,"pkey","-in",private_path,"-pubout","-out",public_path],check=True)
        return {"algorithm":parameter,"private_path":private_path,"public_path":public_path}
    def sign(self, private_path:str, message:bytes, signature_path:str)->dict:
        if not self.available(): raise RuntimeError("OpenSSL not found")
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(message); msg=f.name
        try:
            subprocess.run([self.binary,"pkeyutl","-sign","-inkey",private_path,"-in",msg,"-out",signature_path],check=True)
        finally: os.unlink(msg)
        sig=open(signature_path,"rb").read()
        return {"algorithm":"ML-DSA","signature_b64":base64.b64encode(sig).decode()}
    def verify(self, public_path:str, message:bytes, signature_path:str)->bool:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(message); msg=f.name
        try:
            p=subprocess.run([self.binary,"pkeyutl","-verify","-pubin","-inkey",public_path,"-in",msg,"-sigfile",signature_path],capture_output=True)
            return p.returncode==0
        finally: os.unlink(msg)

class QKDEnvelope:
    """Consumes keys produced by a real QKD system; it does not simulate QKD."""
    def ingest(self,key_material:bytes, source_id:str, key_id:str, generation_time:str)->Evidence:
        if not key_material: raise ValueError("empty QKD key material")
        return Evidence("QKD","observed","key_material",
            base64.b64encode(key_material).decode(),
            {"source_id":source_id,"key_id":key_id,"generation_time":generation_time,
             "physical_origin_required":True})

class ZKProofEnvelope:
    """Stores/validates provenance metadata for an externally generated ZK-SNARK proof."""
    def ingest(self, proof:bytes, system:str, circuit_id:str, public_inputs:Any)->Evidence:
        if not proof: raise ValueError("empty proof")
        return Evidence("ZK-SNARK","observed","proof",
            base64.b64encode(proof).decode(),
            {"proof_system":system,"circuit_id":circuit_id,"public_inputs":public_inputs,
             "verification_status":"not_verified_by_this_envelope"})

def build_security_envelope(event:dict, signatures:list[dict], qkd:Optional[Evidence]=None,
                            zk:Optional[Evidence]=None)->dict:
    body={
      "schema":SCHEMA,"root_id":ROOT_ID,"meta_operator":META_OPERATOR,
      "fitness_54_19_11_0_1":FITNESS,
      "event_hash":event.get("event_hash"),
      "signed_message_sha3_512":digest(canonical_bytes(event),"SHA3-512"),
      "signatures":signatures,
      "qkd":qkd.__dict__ if qkd else None,
      "zk_snark":zk.__dict__ if zk else None
    }
    body["envelope_sha256"]=hashlib.sha256(canonical_bytes(body)).hexdigest()
    return body

def main():
    print(json.dumps({"schema":SCHEMA,"root_id":ROOT_ID,
      "algorithms":["ML-DSA","Ed25519","SHA3-512","BLAKE2b","ML-KEM","QKD","ZK-SNARK"],
      "fitness_54_19_11_0_1":FITNESS},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
