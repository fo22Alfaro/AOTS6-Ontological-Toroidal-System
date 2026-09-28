import unittest
from dimensions.toroidal_core import ToroidalCore

class ToroidalCoreTests(unittest.TestCase):
    def test_dimensions_and_networks(self):
        c=ToroidalCore()
        self.assertEqual(len(c.DIMENSIONS),6)
        for n in c.NETWORKS: self.assertTrue(n)
    def test_interconnection_digest(self):
        c=ToroidalCore()
        c.connect("D1","D2","ONTOLOGICAL")
        c.connect("D2","D3","TOROIDAL")
        c.connect("D3","D5","QUANTUM_RECORD")
        c.connect("D5","D6","CRYPTO")
        self.assertEqual(len(c.digest()),64)

if __name__=="__main__":
 unittest.main()
