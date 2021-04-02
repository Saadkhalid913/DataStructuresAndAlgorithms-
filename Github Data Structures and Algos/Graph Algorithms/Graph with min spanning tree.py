class queue(list):
    def __init__(self):
        super().__init__()

    def add(self, item):
        self.append(item)

    def remove(self):
        if len(self) < 1:
            return
        else:
            return self.pop(0)

    def isempty(self):
        return len(self) == 0


class graph():
    def __init__(self):
        self.edges = {}
        self.edgelist = []
        self.nodes = []

    def __repr__(self):
        return str(self.edges)

    def add(self, *args):
        for node in args:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, a, b, w):
        self.edges[a].append((a, b, w))
        self.edgelist.append((a, b, w))

    def hascycle(self):
        visited = set()
        q = queue()
        q.add(self.nodes[0])
        while not q.isempty():
            node = q.remove()
            if node in visited:
                return True
            else:
                for edge in self.edges[node]:
                    q.add(edge[1])
                visited.add(node)

        return False

    def removeEdge(self, a, b, w):
        self.edgelist.remove((a, b, w))
        self.edges[a].remove((a, b, w))

    def MST(self):
        '''
          returns 2 values, MST sub-graph and cost of MST
        '''
        edges = sorted(
            self.edgelist, key=lambda x: x[2])  # we sort all edges in the graph by weight
        MST = graph()
        MST.add(*self.nodes)
        cost = 0

        for i in range(len(edges)):
            MST.addEdge(*edges[i])  # we add the edge to the mst
            if MST.hascycle():  # if there is a cycle then we remove the edge
                MST.removeEdge(*edges[i])
                continue

            #  if the new edge is valid we include it in our MST
            else:
                cost += edges[i][2]
        return MST, cost


if __name__ == "__main__":
  g = graph()
  g.add(1, 2, 3, 4, 5, 6)
  g.addEdge(1, 2, 6)
  g.addEdge(2, 3, 3)
  g.addEdge(1, 4, 3)
  g.addEdge(1, 5, 2)
  g.addEdge(4, 5, 4)
  g.addEdge(5, 6, 6)
  g.addEdge(3, 6, 8)
  print(g)
  print("\n")

  print(g.MST())
