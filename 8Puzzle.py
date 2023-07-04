from collections import deque

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (row, column)

# Function to check if two states are equal
def are_states_equal(state1, state2):
    for i in range(3):
        for j in range(3):
            if state1[i][j] != state2[i][j]:
                return False
    return True

# Function to get the possible next states
def get_next_states(state):
    next_states = []
    empty_row, empty_col = get_empty_position(state)

    for move in moves:
        new_row = empty_row + move[0]
        new_col = empty_col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            next_states.append(new_state)

    return next_states

# Function to get the position of the empty space (0)
def get_empty_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Breadth-First Search algorithm
def solve_8_puzzle(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if are_states_equal(current_state, goal_state):
            return path

        visited.add(tuple(map(tuple, current_state)))

        for next_state in get_next_states(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Test the program
initial_state = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
solution = solve_8_puzzle(initial_state)

if solution is not None:
    print("Solution found:")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
