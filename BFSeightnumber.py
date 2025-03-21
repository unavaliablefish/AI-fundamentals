from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(initial_state):
    target_state = "12345678x"
    initial_str = ''.join(initial_state.split())
    queue = deque([(initial_str, 0)])  
    visited = set([initial_str])
    while queue:
        current_state, steps = queue.popleft()
        if current_state == target_state:
            return steps
      
        x_index = current_state.index('x')
        x_row, x_col = divmod(x_index, 3)
        
        for dx, dy in directions:
            new_row, new_col = x_row + dx, x_col + dy
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(current_state)
                new_state[x_index], new_state[new_index] = new_state[new_index], new_state[x_index]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
    return -1


initial_state = input().strip()
print(bfs(initial_state))
