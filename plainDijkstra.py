import heapq

def dijkstra(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for x, y, z in edges:
        graph[x].append((y, z))

    distance = [float('inf')] * (n + 1)
    distance[1] = 0
    visited = set()
    while len(visited) < n:
        u = min((i for i in range(1, n + 1) if i not in visited), key=lambda i: distance[i])
        visited.add(u)
        for v, w in graph[u]:
            if v not in visited and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    return distance[n] if distance[n] != float('inf') else -1

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(dijkstra(n, m, edges))
