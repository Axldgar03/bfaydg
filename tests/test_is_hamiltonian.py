from bfaydg import is_hamiltonian
import networkx as nx
def test_is_hamiltonian():
    G = nx.graph_atlas_g()[1]
    assert is_hamiltonian(G) == (0)
    G = nx.graph_atlas_g()[2]
    assert is_hamiltonian(G) == False
    G = nx.graph_atlas_g()[3]
    assert is_hamiltonian(G) == False
