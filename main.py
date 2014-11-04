__author__ = 'Luke Levis'

import networkx as nx
import sys


def overlap(a, b):
    """Return the amount of overlap between the end of string a and the beginning
    of string b. If there is none, 0 is returned.
    """
    for index, val in enumerate(a):
        chop = a[index:]
        amt = len(chop)
        if chop == b[:amt]:
            return amt
    return 0


def make_graph(nodes):
    """Constructs and returns a weighted directed graph from the input list of nodes.
     An edge exists between two nodes u,v if overlap(u,v) != 0. The weight then assigned to
     the edge is the negation of what overlap returns.
    """
    g = nx.DiGraph()

    # add all vertices to graph
    g.add_nodes_from(nodes)

    # assign edge weights
    for node in g.nodes_iter():
        for node2 in g.nodes_iter():
            if node != node2:
                # add iff there if overlap between nodes
                over = overlap(node, node2)
                if over:
                    g.add_edge(node, node2, weight=-over)
    return g


def string_regen(graph):
    """Returns the shortest string obtainable from the given graph.
    Will find a hamiltonian cycle of minimal length.
    """
    # change this line.
    return 0


def main():
    # build list of input vertices and call methods
    list = []
    graph = make_graph(list)
    result = string_regen(graph)

    # write file
    file = open("output.txt", "w")
    file.write(result)

if __name__ == "__main__":
    main()





