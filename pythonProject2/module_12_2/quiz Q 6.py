import networkx as nx

g = nx.Graph()

beatles = ['John Lennon','Paul McCartney','Ringo Starr','George Harrison']

g.add_nodes_from(beatles)
g.add_node('Yoko Ono')

g.add_edges_from([
    ('John Lennon','Paul McCartney'),
    ('John Lennon','Ringo Starr'),
    ('John Lennon', 'George Harrison'),
    ('Paul McCartney', 'Ringo Starr'),
    ('Paul McCartney', 'George Harrison'),
    ('Ringo Starr', 'George Harrison'),
    ('John Lennon', 'Yoko Ono')
])

print(nx.degree_centrality(g))