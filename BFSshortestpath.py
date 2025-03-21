from collections import deque

def bfs_shortest_path(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for x, y in edges:
        graph[x].append(y)
    queue = deque([1])
    distance = [-1] * (n + 1)
    distance[1] = 0
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distance[v] == -1:
                queue.append(v)
                distance[v] = distance[u] + 1
    return distance[n]

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(bfs_shortest_path(n, m, edges))

