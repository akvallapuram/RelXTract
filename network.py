import networkx as nx
import matplotlib.pyplot as plt


def draw_network(relations):
    print("Drawing the network")
    graph = nx.Graph()
    for i in range(len(relations['NODE1'])):
        graph.add_edge(relations['NODE1'][i], relations['NODE2'][i])
    pos = nx.fruchterman_reingold_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_size=2, node_size=150)
    plt.savefig("Results/network.png", format="PNG", dpi=960)
