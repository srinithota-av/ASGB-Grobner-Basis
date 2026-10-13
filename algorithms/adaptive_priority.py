# algorithms/adaptive_priority.py
import networkx as nx

class AdaptivePriorityEvaluator:
    def __init__(self, lambdas=[0.25, 0.25, 0.25, 0.25]):
        """Initializes weights for Signature, Degree, Reduction History, and Dependency."""
        self.lambdas = lambdas
        self.dependency_graph = nx.DiGraph()
        
    def calculate_asi(self, sig_rank, degree, reductions, node_id):
        """Computes the Adaptive Signature Index (ASI) using min-max normalized measures."""
        # Calculate dependency score via in-degree and out-degree from graph G
        if self.dependency_graph.has_node(node_id):
            in_deg = self.dependency_graph.in_degree(node_id)
            out_deg = self.dependency_graph.out_degree(node_id)
            dependency_score = in_deg + out_deg
        else:
            dependency_score = 0
            
        # Mock normalized inputs (Implement full min-max feature mapping across active candidates)
        S = float(sig_rank)
        D = float(degree)
        R = float(reductions)
        P = float(dependency_score)
        
        # Equation (3): Psi = lambda1*S + lambda2*D + lambda3*R + lambda4*P
        psi = (self.lambdas[0] * S + 
               self.lambdas[1] * D + 
               self.lambdas[2] * R + 
               self.lambdas[3] * P)
        return psi

    def update_dependency(self, parent_nodes, child_node):
        """Updates the polynomial dependency graph structural paths."""
        self.dependency_graph.add_node(child_node)
        for parent in parent_nodes:
            self.dependency_graph.add_edge(parent, child_node)
