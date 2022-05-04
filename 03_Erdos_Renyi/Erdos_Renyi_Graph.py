from random import random
import networkx as nx
from networkx import Graph

def erdos_renyi(n, p):
    graph = Graph()
    graph.add_nodes_from(range(n))
    edges = []
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            r = random()
            if r <= p:
                edges.append((i,j))
    graph.add_edges_from(edges)
    return graph

def dfs(graph):
    visited = []
    node_component = dict()
    component = 0
    for node in graph.nodes:
        if node not in visited:
            dfs_visit(node, graph, visited, node_component, component)
            component += 1
    return component

def dfs_visit(node, graph, visited, node_component, component):
    visited.append(node)
    node_component[node] = component
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            dfs_visit(neighbor, graph, visited, node_component, component)


graph = erdos_renyi(30, 0.5)
print("grane rucno generisanog grafa: ", graph.edges)
print("broj grana rucno generisanog grafa: ", graph.number_of_edges())
comp = dfs(graph)
print("postoji ", comp, " komponenti u grafu")
comp_nx_1 = nx.number_connected_components(graph)
print("postoji ", comp_nx_1, " komponenti u nx grafu")

graph_nx = nx.erdos_renyi_graph(30, 0.5)
print("grane networkx grafa: ", graph_nx.edges)
print("broj grana networkx grafa: ", graph_nx.number_of_edges())
comp_nx = dfs(graph_nx)
print("postoji ", comp_nx, " komponenti u nx grafu")
comp_nx_2 = nx.number_connected_components(graph_nx)
print("postoji ", comp_nx_2, " komponenti u nx grafu")
