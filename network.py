import networkx as nx
import matplotlib.pyplot as plt


def draw_network(relations, colors):
    graph = nx.Graph()
    for i in range(len(relations)):
        graph.add_edge(relations[i], edge_color=colors[i])
    nx.draw(graph, with_labels=True)
    plt.show()


relations = [["OBAMA", "TRUMP"], ["UMAKANT", "BINAY"]]
colors = ['r', 'g']
draw_network(relations, colors)
