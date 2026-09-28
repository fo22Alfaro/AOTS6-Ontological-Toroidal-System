import unittest
from crypto import core

class CryptoProtocolTests(unittest.TestCase):
    @unittest.skipUnless(core.CRYPTOGRAPHY_AVAILABLE,"cryptography unavailable")
    def test_ed25519(self):
        sk,pk=core.generate_signing_key(); msg=b"AOTS6"
        sig=core.sign(sk,msg)
        self.assertTrue(core.verify(pk,msg,sig))
        self.assertFalse(core.verify(pk,b"tampered",sig))
    @unittest.skipUnless(core.CRYPTOGRAPHY_AVAILABLE,"cryptography unavailable")
    def test_x25519_hkdf(self):
        a,ap=core.generate_key_exchange_key(); b,bp=core.generate_key_exchange_key()
        self.assertEqual(core.derive_shared_key(a,bp),core.derive_shared_key(b,ap))
    @unittest.skipUnless(core.CRYPTOGRAPHY_AVAILABLE,"cryptography unavailable")
    def test_aead_both(self):
        key=core.secure_token(32)
        for alg in ("AESGCM","CHACHA20POLY1305"):
            nonce,c=core.aead_encrypt(key,b"payload",aad=b"AOTS6",algorithm=alg)
            self.assertEqual(core.aead_decrypt(key,nonce,c,aad=b"AOTS6",algorithm=alg),b"payload")
    def test_hash_hmac_hkdf(self):
        self.assertEqual(len(core.sha256_hex(b"x")),64)
        self.assertEqual(len(core.hmac_sha256(b"k",b"x")),32)
        self.assertEqual(len(core.hkdf_sha256(b"ikm")),32)
    def test_pq_capability_shape(self):
        caps=core.pq_capabilities()
        self.assertEqual(set(caps),{"ML-KEM-768","ML-DSA-65"})

if __name__=="__main__":
 unittest.main()
