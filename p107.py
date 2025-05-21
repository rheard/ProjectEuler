"""
The following undirected network consists of seven vertices and
    twelve edges with a total weight of 243.

https://projecteuler.net/project/images/p107_1.gif

The same network can be represented by the matrix below.

    A   B   C   D   E   F   G
A   -   16  12  21  -   -   -
B   16  -   -   17  20  -   -
C   12  -   -   28  -   31  -
D   21  17  28  -   18  19  23
E   -   20  -   18  -   -   11
F   -   -   31  19  -   -   27
G   -   -   -   23  11  27  -
However, it is possible to optimise the network by removing some edges
    and still ensure that all points on the network remain connected.
    The network which achieves the maximum saving is shown below.
    It has a weight of 93, representing a saving of 243 - 93 = 150
    from the original network.

https://projecteuler.net/project/images/p107_2.gif

Using network.txt, a 6K text file containing a network with forty vertices,
    and given in matrix form, find the maximum saving which can be achieved
    by removing redundant edges whilst ensuring that the network remains
    connected.
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

with open('ProjectEuler/p107_network.txt', 'r') as rb:
    __GRAPH = [[int(entry) if entry != '-' else None
                for entry in line.strip().split(',')]
               for line in rb.readlines()]


def graph_weight(graph):
    """Get the total weight of a graph"""
    return sum(
        edge_weight
        for node_i, node in enumerate(graph)
        for edge_weight in node[:node_i] 
        if edge_weight
    )


def minimum_spanning_forest(graph):
    """
    Return the minimum spanning forest.

    graph should be a graph formatted similar to the table in the problem.
        Unconnected edges should be represented by None or 0. (Preferably None)
    """
    # A tree shall be a dictionary with a set of edges in key 'edges', and
    #   a set of contained verts in the key 'verts'
    # F is a forest of trees, with a tree for each node and no edges.
    F = [{'edges': set(), 'verts': {i}} for i, _ in enumerate(graph)]
    # S is the list of edges.
    S = [(x, y)
         for x, node in enumerate(graph)
         for y, edge in enumerate(node[:x])
         if edge]
    # Sort the edges by weight with the lowest weight ready to be popped off
    #   at the end.
    S = sorted(S, reverse=True, key=lambda edge: graph[edge[1]][edge[0]])

    # Loop while we still have edges and we don't have a spanning forest.
    while S and len(F) > 1:
        edge = S.pop()
        vert1, vert2 = edge

        # Get the tree for the first vertex.
        vert1_tree = [x for x in F if vert1 in x['verts']][0]

        if vert2 not in vert1_tree['verts']:
            # This edge connects 2 trees.
            vert2_tree = [x for x in F if vert2 in x['verts']][0]

            # Remove the second tree, and merge it into the first.
            F.remove(vert2_tree)
            vert1_tree['edges'].add(edge)
            vert1_tree['edges'] |= vert2_tree['edges']
            vert1_tree['verts'] |= vert2_tree['verts']

    # Reconstruct the graph format using the found minimal spanning forest.
    return [
        [edge if any(tuple(sorted((node_i, edge_i), reverse=True)) in tree['edges'] for tree in F) else None
         for edge_i, edge in enumerate(node)]
        for node_i, node in enumerate(graph)
    ]


def solve(graph=None):
    """
    Solving the solution to this problem is also known as the minimum
        spanning tree, finding of which is a classic problem used in several
        fields including energy grid construction.

    After reading Wikipedia:

    1. The optimal algorithm is quite complex, and although it is provably
        optimal, it's runtime is unknown. It relies on using decision trees.

    2. Baruvka's algorithm can be parallized. With a linear amount of
        processors, it has a runtime of O(log n).

    However, I went with Kruskal's algorithm. This problem can be solved easily
        enough without getting into complexities such as decision trees.
        And allocating a pool for a parallized algorithm may very well take
        longer than just solving the darn problem to begin with.
    """
    # Get the difference between the weight of the graph and the weight
    #   of it's minimum spanning forest.
    graph = graph or __GRAPH
    original_weight = graph_weight(graph)
    new_weight = graph_weight(minimum_spanning_forest(graph))
    return original_weight - new_weight


solve.answer = 259679


if __name__ == '__main__':
    output_answer(solve)
