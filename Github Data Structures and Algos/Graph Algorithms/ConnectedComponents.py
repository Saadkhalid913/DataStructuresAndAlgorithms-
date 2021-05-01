from DFS import DFS


def ConnectedComponents(mat):
    count = 0
    visited = []
    for i in range(len(mat)):
        if not i in visited:
            visited += DFS(mat, i)
            count += 1
    return count, set(visited)


mat = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1]
]

print(ConnectedComponents(mat))
