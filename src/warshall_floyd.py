"""
    Warshall floyd is an algorithm for getting minimum path from every node to every node
    We can use this algorithm when there are some edges which has negative weight
    - O(|V|^3)
"""


def warshall_floyd(dist):
    # dist: adjacent matrix
    # prev: prev[i][j] is previous node from j considering minimum path from i to j
    n = len(dist)
    prev = [[i for j in range(n)] for i in range(n)]
    assert n == len(dist[0]), "Illegal dist for adjacent matrix"
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    # print(i, j, k)
                    # print(prev[i][j], prev[k][j])
                    prev[i][j] = prev[k][j]
    # print(prev)
    return dist, prev


def get_warshall_floyd_path(prev, start, end):
    path = []
    while end != start:
        path.append(end)
        end = prev[start][end]
    path.append(start)
    path.reverse()
    return path
