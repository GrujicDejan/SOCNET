import networkx as nx

f = open("Wiki-vote.txt", "r")
f.readline()
f.readline()

noNodes = int(f.readline().strip().split(":")[1].strip().split()[0].strip())
wikiGraph = nx.DiGraph()
wikiGraph.add_nodes_from(range(noNodes))
f.readline()
for line in f:
    nodeFrom = int(line.split("\t")[0].strip())
    nodeTo = int(line.split("\t")[1].strip())
    wikiGraph.add_edge(nodeFrom, nodeTo)

print("Broj grana: ", wikiGraph.number_of_edges())
print("Indegree cvora 3: ", wikiGraph.in_degree(3))
print("Outdegree cvora 4: ", wikiGraph.out_degree(4))
print("Broj slabo povezanih komponenti", nx.number_weakly_connected_components(wikiGraph))
print("Broj jako povezanih komponenti", nx.number_strongly_connected_components(wikiGraph))