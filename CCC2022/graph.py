import typing

class graph():
    def __init__(self, n: int):
        self.edges = [[float("inf") for i in range(n + 1)] for j in range(n + 1)]

    def __repr__(self) -> str:
        return str(self.edges)

    def add(self, a,b,w) -> None:
        self.edges[a][b] = w 
        self.edges[b][a] = w 

    def solve(self, s):
        n = len(self.edges)
        distances = [float("inf") for i in range(n)]
        distances[s] = 0
        visited = [False for i in range(n)]
        nodes = [s]

        while len(nodes) != 0:
            cur = nodes.pop()
            if visited[cur]:
                continue 
            for i in range(n):
                if distances[i] > distances[cur] + self.edges[cur][i]:
                    distances[i] = distances[cur] + self.edges[cur][i]
                    nodes.append(i)
                    visited[cur] = True
                
        return distances



# driver code 

if __name__ == "__main__":
    t = int(input())
    n, m = tuple(map(int, input().split()))
    G = graph(n)

    for i in range(t):
        for _ in range(m):
            a,b,w = tuple(map(int, input().split()))
            G.add(a,b,w)
        s = int(input())

        valid = G.solve(s)

        valid.pop(s)
        valid.pop(0)

        for i in range(len(valid)):
            if valid[i] == float("inf"):
                valid[i] = -1 
        print(*valid)  