import networkx as nx

g = nx.Graph()

g.add_nodes_from(["BWI","DFW","PHX"])

g.add_edges_from([("BWI","DFW", {"price": 100, "time": 3.25}),
                  ("DFW","PHX", {"price": 100, "time": 1.75}),
                  ("BWI","PHX", {"price": 225, "time": 8.0})])
# compute the shortest path based on price
print((nx.dijkstra_path(g, "BWI", "DFW",weight="price")))
print((nx.dijkstra_path_length(g, "BWI", "DFW",weight="price")))

# compute the shortest path based on time
print(nx.dijkstra_path(g, "BWI", "PHX",weight="time"))
print(nx.dijkstra_path_length(g, "BWI", "PHX",weight="time"))