import networkx as nx

#Graph, DiGraph, MultiGraph, MultiBiGraph

g1 = nx.Graph()
g1.add_node(1)
g1.add_nodes_from([2, 3, 4])
g1.add_nodes_from([
    (5, {"color" : "red"}),
    (6, {"color" : "blue"})
])

print(g1.number_of_nodes())

g1.add_edge(1, 2)
print(g1.number_of_edges())
# g1.add_edges_from(lista)

petersenG2 = nx.petersen_graph()
print("Number of nodes: ", petersenG2.number_of_nodes())
print("Number of edges: ", petersenG2.number_of_edges())

usmerenPeters = petersenG2.to_directed()
# print(usmerenPeters.edges())

print("Da li je povezan? ", nx.is_connected(petersenG2))
print("Koliko ima komponenti povezanosti? ", nx.number_connected_components(petersenG2))

print("Da li je jako povezan? ", nx.is_strongly_connected(usmerenPeters))
print("Koliko ima jako povezanih komponenti? ", nx.number_strongly_connected_components(usmerenPeters))

print("Da li je slabo povezan? ", nx.is_weakly_connected(usmerenPeters))
print("Koliko ima slabo povezanih komponenti? ", nx.number_weakly_connected_components(usmerenPeters))

print("Susedi cvora 4 su: ", petersenG2.adj[4])
print("Susedi cvora 4 su: ", petersenG2.neighbors(4))

print("Sepen cvora 4: ", petersenG2.degree[4])
print("Sepen cvorova: ", petersenG2.degree([0, 1, 3]))