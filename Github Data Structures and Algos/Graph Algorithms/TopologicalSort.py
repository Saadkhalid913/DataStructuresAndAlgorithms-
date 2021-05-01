from DFS import DFS


def TopSort(mat):
    n = len(mat[0])
    visited = [False for i in range(n)]
    order = [0 for i in range(n)]
    i = n - 1

    for j in range(n):
        if visited[j]:
            continue
        visitedNodes = DFS(mat, j, [])
        visited[j] = True
        for node in visitedNodes:
            order[i] = node
            i -= 1

    return list(reversed(order))


mat = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
]
print(TopSort(mat))
