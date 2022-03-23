import heapq

"""
    Dijkstra is an algorithm for getting minimum path from one specific node (= start node)
    We cannnot use this algorithm when there are some edges which has negative weight
    - O(|V|^2) when not using heap
    - O(Elog|V|) when using heap
"""


def dijkstra(edges, num_node, start):
    # edges: edges[i] contains [adjacent_node, weight]
    prev = [-1 for i in range(num_node)]
    dist = [float("inf") for i in range(num_node)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [0, 0])
    seen = [False for i in range(num_node)]
    while heap:
        d, nw = heapq.heappop(heap)
        seen[nw] = True
        for nx, w in edges[nw]:
            if not seen[nx] and d + w < dist[nx]:
                dist[nx] = d + w
                heapq.heappush(heap, [d + w, nx])
                prev[nx] = nw
    return dist, prev


def get_dijkstra_path(prev, now):
    path = []
    while now != -1:
        path.append(now)
        now = prev[now]
    path.reverse()
    return path
