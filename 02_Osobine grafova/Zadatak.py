import networkx as nx

f = open("CA-GrQc.txt", "r")
f.readline()
f.readline()

noNodes = int(f.readline().strip().split(":")[1].strip().split()[0].strip())
arxiv = nx.DiGraph()
arxiv.add_nodes_from(range(noNodes))
f.readline()
for line in f:
    nodeFrom = int(line.split("\t")[0].strip())
    nodeTo = int(line.split("\t")[1].strip())
    arxiv.add_edge(nodeFrom, nodeTo)

#in-degree i out-degree za cvor 4, maksimalan stepen cvora
print("Broj grana u grafu: ", arxiv.number_of_edges())
print("Broj cvorova u grafu: ", arxiv.number_of_nodes())
print("In-degree cvora 4: ", arxiv.in_degree(4))
print("Out-degree cvora 4: ", arxiv.out_degree(4))
najveci_indegree = sorted(arxiv.in_degree(), key=lambda x: x[1], reverse=True)[0]
print("Najveci in-degree ima cvor: ", najveci_indegree)
najveci_outdegree = sorted(arxiv.out_degree(), key=lambda x: x[1], reverse=True)[0]
print("Najveci in-degree ima cvor: ", najveci_outdegree)

#komponente povezanosti
largest_wcc = max(nx.weakly_connected_components(arxiv), key=len)
largest_scc = max(nx.strongly_connected_components(arxiv), key=len)
print("Najveca WCC ima cvorova: ", len(largest_wcc))
print("Najveca SCC ima cvorova: ", len(largest_scc))

#k-core (2-core)
arxiv.remove_edges_from(nx.selfloop_edges(arxiv))
dva_core_cvorovi = nx.k_core(G=arxiv, k=2)
dva_core = arxiv.subgraph(dva_core_cvorovi)
print("Broj cvorova u 2-core-u: ", dva_core.number_of_nodes())

#asortativnost mreze
print("Koeficijent asortivnosti mreze: ", nx.degree_assortativity_coefficient(arxiv))

#eigenvector
eigenvector = nx.eigenvector_centrality(arxiv)
eigenvector_sortirano = dict(sorted(eigenvector.items(), key=lambda item: item[1], reverse=True))
print("Eigenvector centralnost (max): ", list(eigenvector_sortirano.keys())[0], ": ", eigenvector_sortirano[list(eigenvector_sortirano.keys())[0]])

#closeness
closeness = nx.closeness_centrality(arxiv)
closeness_sortirano = dict(sorted(closeness.items(), key=lambda item: item[1], reverse=True))
print("Closeness centralnost (max): ", list(closeness_sortirano.keys())[0], ": ", closeness_sortirano[list(closeness_sortirano.keys())[0]])

#betweenness
betweenness = nx.betweenness_centrality(arxiv)
betweenness_sortirano = dict(sorted(betweenness.items(), key=lambda item: item[1], reverse=True))
print("Betweenness centralnost (max): ", list(betweenness_sortirano.keys())[0], ": ", betweenness_sortirano[list(betweenness_sortirano.keys())[0]])

#PagrRank
pagerank = nx.pagerank(arxiv)
pagerank_sortirano = dict(sorted(pagerank.items(), key=lambda item: item[1], reverse=True))
print("Pagerank centralnost (max): ", list(pagerank_sortirano.keys())[0], ": ", pagerank_sortirano[list(pagerank_sortirano.keys())[0]])
