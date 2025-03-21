import heapq

def dijkstra_heap(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for x, y, z in edges:
        graph[x].append((y, z))
    distance = [float('inf')] * (n + 1)
    distance[1] = 0
    pq = [(0, 1)]
    while pq:
        dist, u = heapq.heappop(pq)
        if dist > distance[u]:
            continue
        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                heapq.heappush(pq, (distance[v], v))
    return distance[n] if distance[n] != float('inf') else -1

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(dijkstra_heap(n, m, edges))
