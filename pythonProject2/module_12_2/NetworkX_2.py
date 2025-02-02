# adding nodes to a graph

# nodes can be hashable Python object and can be added to a graph either one, or multiple, at-a-time.
# to add multiple nodes at once, provide a Python iterable container object (list, tuple, set).
# a list of nodes can be retrieved by accessing the nodes instance variable.

import networkx as nx
graph = nx.Graph()

graph.add_node(40) # add an int node
print(graph.nodes) # looks like a list but actually is not a list

# cannot add a non-hashable object
try:
    graph.add_node(set()) # set is unhashable, so I cannot add this to the node for you
except TypeError as e:
    print(e)
# conclusion: key takeaways that any type of node that you want to add to the graph
# it has to be an immutable or a hashable Python object.

# hashable types: integers, floats, strings, tuples
# unhashable types: lists, dictionaries, sets

graph.clear()
print(graph.nodes)

# add multiple nodes at one time
teams = ["Sherlock Holmes", "Ironman", "Batman", "Spider-man"]
graph.add_nodes_from(teams)
print(graph.nodes)

graph.remove_node("Sherlock Holmes")
print(graph.nodes)