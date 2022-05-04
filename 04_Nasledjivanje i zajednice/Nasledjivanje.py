import networkx as nx
import csv

from networkx.algorithms.community import girvan_newman

class DiGraph(nx.DiGraph):
    """
    A model class for graph.
    Attributes
    ----------
    __graph : dict
        Data structure that stores all the graph's nodes and edges.
    """

    def __init__(self, data=None):
        
        if isinstance(data, DiGraph):
            self.__graph = nx.DiGraph(data.__graph)
        else:
            self.__graph = nx.DiGraph()
            edges = []

            with open(data) as csvfile:
                reader = csv.reader(csvfile, delimiter=' ')
                for row in reader:
                    edges.append((int(row[0]), int(row[1])))

            self.__graph.add_nodes_from(range(0, 1005))
            self.__graph.add_edges_from(edges)
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


digraph = DiGraph(data='email-Eu-core.txt')
print('Ucitano ', digraph.nodes_cnt(), ' cvorova i ', digraph.edges_cnt(), ' grana')
gncommiter = girvan_newman(digraph)
gncomm = list(sorted(c) for c in gncommiter)
print(len(gncomm))