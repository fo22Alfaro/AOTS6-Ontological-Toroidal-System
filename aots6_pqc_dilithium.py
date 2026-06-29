from pqcrypto.sign import dilithium5
import hashlib

class AOTS6_Dilithium_Protocol:
    def __init__(self):
        self.sign = dilithium5
        self.public_key, self.private_key = self.sign.generate_keypair()
    def firmar_mensaje(self, mensaje: bytes):
        digest = hashlib.sha3_512(mensaje).digest()
        firma = self.sign.sign(self.private_key, digest)
        return {'public_key': self.public_key.hex(), 'firma': firma.hex()}
    def verificar_firma(self, mensaje: bytes, firma_hex: str, pub_key_hex: str):
        digest = hashlib.sha3_512(mensaje).digest()
        return self.sign.verify(bytes.fromhex(pub_key_hex), digest, bytes.fromhex(firma_hex))
print('AOTS6 Dilithium Protocol loaded - Soberano.')