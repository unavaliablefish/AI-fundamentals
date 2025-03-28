def dfs(start, end, max_depth):
    start = ''.join(start)
    end = ''.join(end)
    if start == end:
        return 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set([start])

    def dfs_recursive(state, steps):
        if steps > max_depth:
            return 0
        zero_index = state.index('x')
        x, y = zero_index // 3, zero_index % 3
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_index = nx * 3 + ny
                new_state = list(state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                new_state = ''.join(new_state)
                if new_state == end:
                    return 1
                if new_state not in visited:
                    visited.add(new_state)
                    if dfs_recursive(new_state, steps + 1):
                        return 1
                    visited.remove(new_state)
        return 0

    return dfs_recursive(start, 0)



start_state = input().split()
goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', 'x']
max_depth = 30
result = dfs(start_state, goal_state, max_depth)
print(result)


