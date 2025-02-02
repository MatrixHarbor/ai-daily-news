import networkx as nx

graph = nx.Graph()

# Accessing Nodes in a Graph
# dictionary
teams = [("Eagles", {"record": "16-0"}),
         ("Cowboys", {"record": "0-16"})]

graph.add_nodes_from(teams)  # add nodes to graph

teams = graph.nodes # get a NodeView object

print(f"{type(teams)}:\n{teams}\n")

print(teams["Eagles"])
print(teams["Cowboys"])

print(f"\n{teams.data()}\n")

for team in graph.nodes.data():
    print(team[1]["record"])