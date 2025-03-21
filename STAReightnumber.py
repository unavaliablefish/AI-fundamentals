import heapq


directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]


def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] == 'x':
            continue
        num = int(state[i]) - 1
        distance += abs(i // 3 - num // 3) + abs(i % 3 - num % 3)
    return distance


def a_star(initial_state):
  
    target_state = "12345678x"
    

    initial_str = ''.join(initial_state.split())
    
  
    priority_queue = [(manhattan_distance(initial_str), 0, initial_str, '')] 
    visited = set([initial_str])
    
    while priority_queue:
        _, steps, current_state, path = heapq.heappop(priority_queue)
        
    
        if current_state == target_state:
            return path
        
      
        x_index = current_state.index('x')
        x_row, x_col = divmod(x_index, 3)
        
 
        for dx, dy, action in directions:
            new_row, new_col = x_row + dx, x_col + dy
            if 0 <= new_row < 3 and 0 <= new_col < 3:
            
                new_index = new_row * 3 + new_col
             
                new_state = list(current_state)
                new_state[x_index], new_state[new_index] = new_state[new_index], new_state[x_index]
                new_state = ''.join(new_state)
                
             
                if new_state not in visited:
                    visited.add(new_state)
                    heapq.heappush(priority_queue, (manhattan_distance(new_state) + steps + 1, steps + 1, new_state, path + action))
    
   
    return "unsolvable"


initial_state = input().strip()


print(a_star(initial_state))