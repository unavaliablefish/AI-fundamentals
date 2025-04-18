import matplotlib.pyplot as plt
import heapq
import math
import time

# 定义启发式函数
def heuristic(a, b, method="manhattan"):
    if method == "manhattan":  # 曼哈顿距离
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    elif method == "euclidean":  # 欧几里得距离
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    elif method == "diagonal":  # 对角线距离
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
    else:
        raise ValueError("Unknown heuristic method: {}".format(method))

# A* 算法实现
def a_star_search(maze, start, end, heuristic_method="manhattan", visualize=False, ax=None):
    rows = len(maze)
    cols = len(maze[0])
    visited = set()
    parent = {}
    g_score = {start: 0}  
    f_score = {start: heuristic(start, end, method=heuristic_method)}
    priority_queue = [(f_score[start], start)]  
    
    while priority_queue:
        current_f, now = heapq.heappop(priority_queue)
        
        if now in visited:
            continue
        visited.add(now)
        
        if visualize:
            ax.scatter(now[1], now[0], s=100, color='cyan', alpha=0.7, zorder=2)
            plt.draw()
            plt.pause(0.1)  

        if now == end:
            path = []
            while now in parent:
                path.append(now)
                now = parent[now]
            path.append(start)
            return path[::-1], visited
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        for dx, dy in directions:
            x = now[0] + dx
            y = now[1] + dy
            adj = (x, y)
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and adj not in visited:
                tentative_g_score = g_score[now] + 1  
                if adj not in g_score or tentative_g_score < g_score[adj]:
                    parent[adj] = now
                    g_score[adj] = tentative_g_score
                    f_score[adj] = tentative_g_score + heuristic(adj, end, method=heuristic_method)
                    heapq.heappush(priority_queue, (f_score[adj], adj))
    
    return None, visited

# 可视化迷宫和路径
def visualize_maze_with_path(maze, path=None, visited=None, title=""):
    plt.figure(figsize=(len(maze[0]), len(maze))) 
    plt.imshow(maze, cmap='Greys', interpolation='nearest')  

    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o', markersize=8, color='red', linewidth=3)

    if visited:
        for x, y in visited:
            plt.scatter(y, x, s=50, color='cyan', alpha=0.5, zorder=1)

    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

    plt.title(title)
    plt.axis('on')  
    plt.show()

# 比较三种启发式函数的效率
def compare_heuristics(maze, start, end, visualize=False):
    heuristics = ["manhattan", "euclidean", "diagonal"]
    results = {}

    for heuristic_method in heuristics:
        fig, ax = plt.subplots(figsize=(len(maze[0]), len(maze)))
        ax.imshow(maze, cmap='Greys', interpolation='nearest')
        ax.set_xticks(range(len(maze[0])))
        ax.set_yticks(range(len(maze)))
        ax.set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
        ax.set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
        ax.axis('on')

        start_time = time.time()
        path, visited = a_star_search(maze, start, end, heuristic_method=heuristic_method, visualize=visualize, ax=ax)
        end_time = time.time()
        run_time = end_time - start_time
        path_length = len(path) if path else 0

        results[heuristic_method] = {"run_time": run_time, "path_length": path_length}

        if visualize:
            visualize_maze_with_path(maze, path=path, visited=visited, title=f"Heuristic: {heuristic_method.capitalize()}")
    
    return results

# 主函数
if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    comparison_results = compare_heuristics(maze, start, end, visualize=True)

    for heuristic, result in comparison_results.items():
        print(f"Heuristic: {heuristic}")
        print(f"  Run Time: {result['run_time']:.4f} seconds")
        print(f"  Path Length: {result['path_length']}")