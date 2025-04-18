import matplotlib.pyplot as plt
import numpy as np

# 迷宫类
class Maze:
    def __init__(self, maze):
        self.maze = np.array(maze)
        self.rows, self.cols = self.maze.shape
        self.obstacles = self._find_obstacles()

    def _find_obstacles(self):
        return set(zip(*np.where(self.maze == 1)))

    def is_obstacle(self, position):
        return position in self.obstacles

# 启发式函数
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# IDA* 算法
def ida_star(maze, start, end, visualize=False, ax=None):
    bound = heuristic(start, end)
    while True:
        t, path, visited = search(maze, start, end, 0, bound, visualize, ax)
        if t == "FOUND":
            return path, visited
        if t == float('inf'):
            return None, visited
        bound = t

def search(maze, node, end, g, bound, visualize, ax):
    f = g + heuristic(node, end)
    if f > bound:
        return f, None, None
    if node == end:
        return "FOUND", [node], {node}
    
    min = float('inf')
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = {node}
    path = [node]
    
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        adj = (x, y)
        if 0 <= x < maze.rows and 0 <= y < maze.cols and maze.maze[x, y] == 0 and adj not in visited:
            visited.add(adj)
            path.append(adj)
            if visualize:
                ax.scatter(y, x, s=100, color='cyan', alpha=0.7, zorder=2)
                plt.draw()
                plt.pause(0.1)
            t, p, v = search(maze, adj, end, g + 1, bound, visualize, ax)
            if t == "FOUND":
                return "FOUND", p, v
            if t < min:
                min = t
            visited.remove(adj)
            path.pop()
    
    return min, path, visited

# 可视化迷宫和路径
def visualize_maze_with_path(maze, path=None, visited=None, obstacles=None):
    fig, ax = plt.subplots(figsize=(len(maze[0]), len(maze)))
    ax.imshow(maze, cmap='Greys', interpolation='nearest')
    
    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_y, path_x, marker='o', markersize=8, color='red', linewidth=3)
    
    if visited:
        for x, y in visited:
            ax.scatter(y, x, s=50, color='cyan', alpha=0.5, zorder=1)
    
    if obstacles:
        for x, y in obstacles:
            ax.scatter(y, x, s=50, color='blue', alpha=0.5, zorder=1)
    
    ax.set_xticks(range(len(maze[0])))
    ax.set_yticks(range(len(maze)))
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.axis('on')
    return fig, ax

# 主函数
if __name__ == "__main__":
    # 创建一个预先定义的迷宫
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    maze = np.array(maze)
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)

    maze_obj = Maze(maze)
    fig, ax = visualize_maze_with_path(maze_obj.maze, obstacles=maze_obj.obstacles)
    ax.imshow(maze_obj.maze, cmap='Greys', interpolation='nearest')
    ax.set_xticks(range(len(maze_obj.maze[0])))
    ax.set_yticks(range(len(maze_obj.maze)))
    ax.set_xticks([x - 0.5 for x in range(1, len(maze_obj.maze[0]))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(maze_obj.maze))], minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.axis('on')

    path, visited = ida_star(maze_obj, start, end, visualize=True, ax=ax)

    visualize_maze_with_path(maze_obj.maze, path=path, visited=visited, obstacles=maze_obj.obstacles)
    plt.show()