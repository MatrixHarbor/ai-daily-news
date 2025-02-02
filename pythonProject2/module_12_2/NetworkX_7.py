# Degree Centrality
# how popular/important people are in the social network
import networkx as nx
# social network
g = nx.Graph()

g.add_nodes_from(["Joe","Alan","My Katie","Mantu"])

g.add_edges_from([("Joe","Alan"),
                  ("Joe","My Katie"),
                  ("Joe","Mantu")])

centrality = nx.degree_centrality(g)

for n in g.nodes():
    print(f"{n}: {centrality[n]}")

# build your directed graph to model the flow problem
# when you actually go to run the max-flow algorithm to complete the assignment,
# it's going to actually take you only about a line or two of code to do.
# Most of the difficulty is more along the lines of getting acclimated to the NetworkX library.
# Understand how NetworkX library works and constructing your graph