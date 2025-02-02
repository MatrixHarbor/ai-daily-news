# create graphs that we can interact with

import networkx as nx

# undirected graph
graph = nx.Graph() # empty graph

# directed graph
digraph = nx.DiGraph() # start with an empty graph

# multi graph allows parallel edges: two edges between a single pair
multi_graph = nx.MultiGraph()

# star graph (built-in) graph generator
star_graph = nx.star_graph(5)

# barbell graph (built-in)
barbell_graph = nx.barbell_graph(4,1)
# barbell_graph = nx.barbell_graph(4)

print(star_graph)
print(barbell_graph)
print(star_graph.nodes)
print(star_graph.edges)