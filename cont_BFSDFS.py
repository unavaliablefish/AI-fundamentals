import sys
from collections import deque
import numpy as np

# 传统 BFS 实现
def bfs_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([start])
    
    while queue:
        now = queue.popleft()
        if now in visited:
            continue
        visited.add(now)
        
        if now == end:
            return visited
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x, y = now[0] + dx, now[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and (x, y) not in visited:
                queue.append((x, y))
    
    return visited

# 传统 DFS 实现
def dfs_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    stack = [start]
    
    while stack:
        now = stack.pop()
        if now in visited:
            continue
        visited.add(now)
        
        if now == end:
            return visited
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x, y = now[0] + dx, now[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and (x, y) not in visited:
                stack.append((x, y))
    
    return visited

# 使用位图的 BFS 实现
def bfs_search_bit(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = np.zeros(rows * cols, dtype=bool)  # 初始化位图
    queue = deque([start])
    
    while queue:
        now = queue.popleft()
        if visited[now[0] * cols + now[1]]:
            continue
        visited[now[0] * cols + now[1]] = True
        
        if now == end:
            return visited
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x, y = now[0] + dx, now[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and not visited[x * cols + y]:
                queue.append((x, y))
    
    return visited

# 使用位图的 DFS 实现
def dfs_search_bit(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = np.zeros(rows * cols, dtype=bool)  # 初始化位图
    stack = [start]
    
    while stack:
        now = stack.pop()
        if visited[now[0] * cols + now[1]]:
            continue
        visited[now[0] * cols + now[1]] = True
        
        if now == end:
            return visited
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x, y = now[0] + dx, now[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and not visited[x * cols + y]:
                stack.append((x, y))
    
    return visited

# 比较内存占用
def compare_memory_usage(maze, start, end):
    print("Comparing memory usage for BFS and DFS with traditional and bit array implementations...")
    
    # BFS 传统实现
    visited_bfs = bfs_search(maze, start, end)
    bfs_memory = sys.getsizeof(visited_bfs)
    
    # BFS 位图实现
    visited_bfs_bit = bfs_search_bit(maze, start, end)
    bfs_bit_memory = sys.getsizeof(visited_bfs_bit)
    
    # DFS 传统实现
    visited_dfs = dfs_search(maze, start, end)
    dfs_memory = sys.getsizeof(visited_dfs)
    
    # DFS 位图实现
    visited_dfs_bit = dfs_search_bit(maze, start, end)
    dfs_bit_memory = sys.getsizeof(visited_dfs_bit)
    
    print(f"BFS traditional: {bfs_memory} bytes")
    print(f"BFS with bit array: {bfs_bit_memory} bytes")
    print(f"DFS traditional: {dfs_memory} bytes")
    print(f"DFS with bit array: {dfs_bit_memory} bytes")

# 测试迷宫
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

compare_memory_usage(maze, start, end)