class Queue(list):
    def __init__(self):
        super().__init__()

    def add(self, value):
        self.append(value)

    def remove(self):
        return self.pop(0)

    def isempty(self):
        return len(self) <= 0


class Stack(list):

    def __init__(self):
        super().__init__()

    def add(self, value):
        self.append(value)

    def remove(self):
        return self.pop()


class Graph():

    def __init__(self):

        self.edges = dict()
        self.nodes = []

    def addNode(self, node):
        assert node not in self.nodes, 'node already exists'

        self.nodes.append(node)
        self.edges[node] = []

    def addEdge(self, FromNode, ToNode, Weight):
        assert FromNode in self.nodes and ToNode in self.nodes, 'Node not in graph'
        # edges are represented as a tuple with format (ToNode, EdgeWeight)
        self.edges[FromNode].append((ToNode, Weight))

    def Dijkstra(self, StartNode):
        '''
            Algorithm which returns dict of shortest paths to each node in graph from a starting node
        '''
        assert StartNode in self.nodes, 'Node not in graph'

        distances = {node: float("inf") for node in self.nodes}
        distances[StartNode] = 0

        visited = set()
        Q = Queue()
        Q.add(StartNode)

        while not Q.isempty():
            node = Q.remove()
            visited.add(node)

            for edge in self.edges[node]:
                # unpacking information from the edge tuple
                neighbor, neighborWeight = edge
                # if we have already visited the node, there is no need to visit it again, or else we will loop forever
                if neighbor in visited:
                    continue
                # Compare distance of the node we are visting plus the distance to a neighbor, with the currently recorded distance
                # to the neighbor. If the former is lesser, it becomes the new shortest distance
                if distances[node] + neighborWeight < distances[neighbor]:
                    distances[neighbor] = distances[node] + neighborWeight
                # Adding the neighbor into the queue to be visited
                Q.add(neighbor)

        return distances


g = Graph()
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode(4)


g.addEdge(1, 2, 10)
g.addEdge(2, 4, 8)
g.addEdge(1, 4, 20)
print(g.edges)
print(g.Dijkstra(1))
