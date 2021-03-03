class Queue(list):
    def __init__(self):
        super().__init__()

    def add(self, value):
        self.append(value)

    def remove(self):
        return self.pop(0)


class PriorityQueue(self):
    def __init__(self):
        self.data = []

    def add(self, item: tuple):
        if len(self.data) <= 1:
            self.data.append(item)

        else:
            i = 0
            while item[1] < self.data[i][1]:
                i += 1
            self.data.insert(i, item)

    def remove(self):
        return self.data.pop(0)

    def isEmpty(self):
        return len(self.data > 0)


class Graph():

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add(self, node):
        assert node not in self.nodes
        self.nodes.append(node)
        self.edges[node] = []

    def AddEdge(self, Node1, Node2):
        assert Node1 in self.nodes and Node2 in self.nodes
        self.edges[Node1].append(Node2)

    def BFS(self, node):
        ''' 

            Breadth first search algorithm starting at a given node

        '''

        assert node in self.nodes

        # Where we store the nodes
        NodesFound = []

        # We make sure there are no duplicated
        visited = set()

        # We insert nodes into queue with lower depth nodes at a higher priority (inserted first)
        Q = Queue()

        # We add the starting node to the queue
        Q.add(node)

        # We run the loop until we run our of unique nodes
        while len(Q) != 0:

            # We look at the neighbors of the most recently removed node
            node = Q.remove()
            NodesFound.append(node)
            visited.add(node)
            for neighbor in self.edges[node]:
                # We continue the loop if we have already visited one of the neighbors
                if neighbor in visited:
                    continue

                # We set up the neighbor to be visited if we have not yet visited it
                Q.add(neighbor)

        return NodesFound

    def DFS(self, node, nodes=[]):
        '''
            Depth first search starting at a given node
        '''

        assert node in self.nodes

        for neighbor in self.edges[node]:
            if neighbor in nodes:
                continue

            nodes.append(neighbor)
            self.DFS(neighbor, nodes)

        return nodes


G = Graph()

G.add(0)
G.add(1)
G.add(2)
G.add(3)

G.AddEdge(2, 3)
G.AddEdge(0, 1)
G.AddEdge(2, 0)
G.AddEdge(0, 2)
G.AddEdge(3, 3)
G.AddEdge(1, 2)

print(G.DFS(1))
