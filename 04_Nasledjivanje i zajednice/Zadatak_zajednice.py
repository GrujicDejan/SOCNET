import networkx as nx
import csv

from networkx.algorithms.community import label_propagation_communities

class Graph:
    """
    A model class for graph.
    Attributes
    ----------
    __graph : dict
        Data structure that stores all the graph's nodes and edges.
    """

    def __init__(self, data=None):
        
        if isinstance(data, Graph):
            self.__graph = nx.Graph(data.__graph)
        else:
            self.__graph = nx.read_gml(data)

    def nodes(self):
        return list(self.__graph.nodes(data=True))

    def edges(self, node=None):
        return list(
            self.__graph.edges()
            if node == None
            else self.__graph.edges(node)
        )

    def nodes_cnt(self):
        return len(self.__graph)

    def edges_cnt(self):
        return len(self.__graph.edges)

   
    def add_node(self, id):
        self.__graph.add_node(id)

    def add_edge(self, node1, node2):
        self.__graph.add_edge(node1, node2)

    def has_edge(self, node1, node2):
        return self.__graph.has_edge(node1, node2)

    def to_networkx(self):
        return self.__graph


graph = Graph(data='dolphins.gml')
print('Ucitano ', graph.nodes_cnt(), ' cvorova i ', graph.edges_cnt(), ' grana')
gncommiter = label_propagation_communities(graph.to_networkx())
gncomm = list(sorted(c) for c in gncommiter)
print(len(gncomm))