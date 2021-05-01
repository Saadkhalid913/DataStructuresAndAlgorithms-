class Graph():

    def __init__(self):
        self.adjacencylist = {}
        self.nodes = []
        self.edgesNum = 0
        self.nodesNum = 0

    def __contains__(self, node):
        return node in self.nodes

    def __repr__(self):
        return str(self.adjacencylist)

    def __iter__(self):
        return iter(self.nodes)

    def add(self, *args):
        for node in args:
            if node in self:
                pass
            else:
                self.nodes.append(node)
                self.adjacencylist[node] = {}
                self.nodesNum += 1

    def view(self):
        for node in self:
            print(f"{node}: {self.adjacencylist[node]}")

    def addedge(self, a, b, weight: int):
        assert a in self and b in self, "Both nodes must be in graph"
        self.adjacencylist[a][b] = weight
        self.edgesNum += 1

    def BelmanFord(self, start: int, end: int):
        D = [float("inf") for i in range(self.nodesNum)]
        D[start] = 0
        for node in self.nodes:
            for edge in self.adjacencylist[node]:
                if D[edge] > D[node] + self.adjacencylist[node][edge]:
                    print(True)
                    D[edge] = D[node] + self.adjacencylist[node][edge]

        print(D)


G = Graph()

G.add(0, 1, 2, 3)
G.addedge(1, 2, 10)
G.BelmanFord(1, 2)


G.view()
