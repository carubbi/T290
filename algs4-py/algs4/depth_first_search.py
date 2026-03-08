"""
  Execution:    python -m algs4.depth_first_search filename.txt s
  Data files:   ../dataset/tinyG.txt
                ../dataset/mediumG.txt

  Run depth first search on an undirected graph.
  Runs in O(E + V) time.

 % python -m algs4.depth_first_search ../dataset/tinyG.txt 0
  0 1 2 3 4 5 6
  NOT connected

 % python -m algs4.depth_first_search ../dataset/tinyG.txt 9
  9 10 11 12
  NOT connected

 """
from algs4.graph import Graph


class DepthFirstSearch:

    def __init__(self, G, s):
        self.marked = [False for _ in range(G.V)]
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    s = int(sys.argv[2])
    V = int(f.readline())
    E = int(f.readline())
    g = Graph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    search = DepthFirstSearch(g, s)
    for v in range(g.V):
        if search.marked[v]:
            print(str(v) + " ")
    if search.count == g.V:
        print("connected")
    else:
        print("not connected")
