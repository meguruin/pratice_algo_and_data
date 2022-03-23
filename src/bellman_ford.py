"""
    Bellman Ford is an algorithm for getting minimum path from one specific node (= start node)
    We can use this algorithm when there are some edges which has negative weight
    - O(|V||E|)
"""


def bellman_ford(edges, num_node, start):
    # edges: list that contains(from, to, cost)
    # prev: prev[i][j] is previous node from j considering minimum path from i to j
    prev = [-1 for i in range(num_node)]
    dist = [float("inf") for i in range(num_node)]
    dist[start] = 0
    for i in range(num_node):
        update = False
        for edge in edges:
            p1, p2, w = edge
            if dist[p1] + w < dist[p2]:
                dist[p2] = dist[p1] + w
                prev[p2] = p1
                update = True
        if not update:
            break
        if i == num_node - 1:
            return -1, -1
    return dist, prev


def get_bellman_ford_path(prev, now):
    path = []
    while now != -1:
        path.append(now)
        now = prev[now]
    path.reverse()
    return path
