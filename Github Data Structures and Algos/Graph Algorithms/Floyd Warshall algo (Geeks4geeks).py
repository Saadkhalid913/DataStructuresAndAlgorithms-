class Graph():

    def __init__(self, AdjMatrix: list):
        self.edges = AdjMatrix

    def FloydWarshal(self):
        for i in range(len(self.edges)):
            # This loop is the outermost layer of the algorithm, in this loop, we go though all the possible vertices in the graph, and
            # we try to see if using the vertex i as a "bridge" between vertex j and k will produce a shorter path than going from
            # j to k directly. If that condition is true, we update the adjacency matrix. We assume that the each the vertices of the graph
            # are numbers {0,1,2...n-1} where n is the number of vertices, or the dimention of the adjacency matrix

            for j in range(len(self.edges)):
                # This second loop is for the row of the adjacency matrix we are visiting, in other words, it is the "ToNode"
                # in the comparison we will do in the following loop
                for k in range(len(self.edges)):
                    # k is the index of the node that we are visiting from node j, since this is a directed graph, we assume that a path
                    # from j -> k is not necessarily the same as the path from k -> j

                    # self.edges[j][k] is the path recorded in the adjacency matrix. it is the shortest current path from node j to k
                    # we compare the path j -> k to the path j -> i -> k, i acts as the "bridge" between the two nodes.
                    #
                    if self.edges[j][k] > self.edges[j][i] + self.edges[i][k]:
                        self.edges[j][k] = self.edges[j][i] + self.edges[i][k]

        return self.edges


g = Graph([[0, 5, float("inf"), 10],
           [float("inf"), 0, 3, float("inf")],
           [float("inf"), float("inf"), 0, 1],
           [float("inf"), float("inf"), float("inf"), 0]])

for i in range(len(g.edges)):
    print(g.FloydWarshal()[i])
