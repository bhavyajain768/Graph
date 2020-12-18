import networkx
G = networkx.Graph()
G.add_nodes_from([1,2,3])
G.add_edges_from([(1,2),(1,3),(2,3)])
n = G.number_of_nodes()
e = G.number_of_edges()
node = G.nodes()
edge = G.edges()
print(n,node,e,edge)