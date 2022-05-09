"""
    Prim:
        - Appending the most small edge among seen nodes
        - Using heapq
    Kruskal:
        - Checking all edges in ascending order and appending edge if it connects to new node
        - Using Union-Find Tree
    O(ElogV)
"""
import heapq
from src import UnionFind

def prim(edges, num_nodes):
    # edges: adjacent list
    heap = []
    visited = [False for i in range(num_nodes)]
    heapq.heappush(heap, [0, 0])
    cost = 0
    connection = 0
    while heap:
        w, nx = heapq.heappop(heap)
        if visited[nx]:
            continue
        cost += w
        connection += 1
        visited[nx] = True
        for edge in edges[nx]:
            heapq.heappush(heap, [edge[1], edge[0]])
        if connection == num_nodes:
            break
    return cost


def kruskal(edges, num_nodes):
    # edges: simple edge list such as (from, to, cost)
    uf = UnionFind(num_nodes)
    edges = [(w, n1, n2) for (n1, n2, w) in edges]
    edges.sort()
    cost = 0
    for edge in edges:
        w, n1, n2 = edge
        if uf.issame(n1, n2):
            continue
        uf.unite(n1, n2)
        cost += w
    return cost
