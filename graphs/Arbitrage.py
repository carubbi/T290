# Created for BADS 2018
# See README.md for details
# Python 3

import math
import sys


def main():
    """The Arbitrage function provides a client that finds an arbitrage
    opportunity in a currency exchange table by constructing a complete-digraph
    representation of the exchange table and then finding a negative cycle in
    the digraph.

    This implementation uses the Bellman-Ford algorithm to find a negative cycle in
    the complete digraph. The running time is proportional to V3 in the worst case,
    where V is the number of currencies.

    For additional documentation, see Section 4.4 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.

    """
    from graphs import BellmanFordSP
    from graphs import DirectedEdge
    from graphs import EdgeWeightedDigraph
    from stdlib import readInt, readString, readFloat
    
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")

    # V currencies
    V = readInt()
    name = [None] * V

    # Create complete network
    graph = EdgeWeightedDigraph(V)
    for v in range(V):
        name[v] = readString()
        for w in range(V):
            rate = readFloat()
            edge = DirectedEdge(v, w, -math.log(rate))
            graph.add_edge(edge)

    # find negative cycle
    spt = BellmanFordSP(graph, 0)
    if spt.has_negative_cycle():
        stake = 1000.0
        for edge in spt.negative_cycle():
            print("{} {}", stake, name[edge.from_vertex()])
            stake *= math.exp(-edge.weight())
            print("{} {}")


if __name__ == "__main__":
    main()