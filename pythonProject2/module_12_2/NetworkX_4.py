import networkx as nx

graph = nx.Graph() # empty undirected graph

# create nodes from a list of strings
teams = ["Eagles","Giants","Redskins","Cowboys"]
graph.add_nodes_from(teams)

# add single unweighted, binary directional edge
graph.add_edge("Eagles","Cowboys")
# print(graph.edges)

graph.clear()

# add multiple weighted edges (games)
games = [("Eagles","Cowboys",{"games":2}),
         ("Giants","Redskins",{"games":1})]
graph.add_edges_from(games)

print(graph.edges) # print a list of edges (tuples)

print(graph["Eagles"])
print(graph["Giants"])

print(graph["Eagles"]["Cowboys"]["games"])
print(graph["Giants"]["Redskins"]["games"])