import unittest
from net.toroidal_net import Cell,ToroidalAutomata,NemesisDefense,Node,attest

class NetTests(unittest.TestCase):
    def test_cellular_step_and_digest(self):
        cells=[Cell("a",1,{"b"}),Cell("b",1,{"a","c"}),Cell("c",0,{"b"})]
        ca=ToroidalAutomata(cells)
        self.assertEqual(ca.step(),{"a":1,"b":1,"c":1})
        self.assertEqual(len(ca.topology_digest()),64)
    def test_nemesis_is_bounded_and_authorized(self):
        n=NemesisDefense(2)
        signals=[{"node_id":"a","recommended_action":"isolate","authorization":True},
                 {"node_id":"b","recommended_action":"quarantine","authorization":True},
                 {"node_id":"c","recommended_action":"isolate","authorization":True},
                 {"node_id":"x","recommended_action":"delete","authorization":True}]
        self.assertEqual(len(n.plan(signals)),2)
    def test_attestation_is_metadata(self):
        self.assertEqual(attest(Node("a","MX","abc"))["attestation"],"metadata_only")

if __name__=="__main__": unittest.main()
