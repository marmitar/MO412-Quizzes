import networkx as nx
from matplotlib import pyplot as plt


def random(n: int, p: float) -> nx.Graph:
    return nx.gnp_random_graph(n, p, seed=0x1234, directed=False)

def layout(graph: nx.Graph):
    return nx.kamada_kawai_layout(graph)
    return nx.nx_agraph.graphviz_layout(graph, prog='dot')

if __name__ == '__main__':
    graph = random(6, 0.7)

    nx.draw(graph, pos=layout(graph))
    plt.savefig('graph.svg')
    # plt.show(block=True)
