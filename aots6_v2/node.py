"""
AOTS6 v2 - Node Runtime
Local execution unit for distributed AOTS6 systems
"""

from ontology import Ontology
from engine import Engine

class Node:
    def __init__(self):
        self.ontology = Ontology()
        self.engine = Engine()
        self.state = {"value": 0}

    def step(self, input_data):
        K = self.ontology.gamma(self.state)
        self.state = self.engine.F(self.state, K)
        return self.state
