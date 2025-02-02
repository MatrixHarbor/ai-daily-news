import networkx as nx


graph = nx.Graph()
digraph = nx.DiGraph()

teams = ("Eagles", "Cowboys") # strings are immutable / hashable
graph.add_nodes_from(teams)

# games = [("Eagles","Cowboys",{"games":2}),
#          ("Giants","Redskins",{"games":1})]
# graph.add_edges_from(games)
# add unweighted directed edge from Eagles to Cowboys
digraph.add_edge(teams[0],teams[1])

# print(type(graph.edges))
# print(graph.edges)
print(digraph.edges)

print(("Cowboys","Eagles") in digraph.edges)
# does this edge (from Cowboys to Eagles) exist in digraph, the result is False
# False: because the edge goes from Eagles to Cowboys. uni-directional
