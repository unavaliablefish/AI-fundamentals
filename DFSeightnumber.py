def inversion_number(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] != 'x' and arr[j] != 'x' and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def is_solvable(initial_state):
    state = initial_state.split()
    inv_count = inversion_number(state)
    return 1 if inv_count % 2 == 0 else 0

initial_state = input().strip()

print(is_solvable(initial_state))