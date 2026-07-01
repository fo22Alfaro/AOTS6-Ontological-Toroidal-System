"""
AOTS6 v2 - Ontology Module
Formal semantic graph representation layer
Autor: Alfredo Jhovany Alfaro Garcia
"""

class Ontology:
    def __init__(self):
        self.K = {
            "nodes": {},
            "edges": []
        }

    def add_node(self, node_id, data):
        self.K["nodes"][node_id] = data

    def add_edge(self, src, dst, relation="rel"):
        self.K["edges"].append({
            "from": src,
            "to": dst,
            "type": relation
        })

    def gamma(self, state):
        node_id = f"s_{len(self.K['nodes'])}"
        self.add_node(node_id, {
            "state": str(state),
            "weight": len(str(state))
        })

        if len(self.K["nodes"]) > 1:
            prev = list(self.K["nodes"].keys())[-2]
            self.add_edge(prev, node_id, "evolves_to")

        return self.K
