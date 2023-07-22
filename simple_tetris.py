import random
import time

# Tetris shapes and their rotations
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6],
     [6, 6]],

    [[7, 7, 7, 7]]
]

# Console colors for each shape
SHAPE_COLORS = {
    1: '\033[91m',  # Red
    2: '\033[92m',  # Green
    3: '\033[93m',  # Yellow
    4: '\033[94m',  # Blue
    5: '\033[95m',  # Magenta
    6: '\033[96m',  # Cyan
    7: '\033[97m'   # White
}

def create_grid():
    return [[0 for _ in range(10)] for _ in range(20)]

def print_grid(grid, current_shape, shape_position):
    clear_console()
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if (i, j) in shape_position:
                print(SHAPE_COLORS[current_shape], '█', end=' ')
            else:
                print('\033[90m' if val == 0 else SHAPE_COLORS[val], '█', end=' ')
        print()
    print('\033[0m' + '=' * 21)

def clear_console():
    print("\033[H\033[J", end='')

def check_collision(grid, shape, shape_position):
    for x, y in shape_position:
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return True
        if grid[x][y] != 0:
            return True
    return False

def merge_shape(grid, shape, shape_position, shape_id):
    for x, y in shape_position:
        grid[x][y] = shape_id

def remove_completed_lines(grid):
    lines_to_remove = [i for i, row in enumerate(grid) if all(row)]
    for i in lines_to_remove:
        grid.pop(i)
        grid.insert(0, [0 for _ in range(10)])

def rotate_shape(shape):
    return list(zip(*reversed(shape)))

def main():
    grid = create_grid()
    score = 0

    while True:
        current_shape = random.choice(SHAPES)
        shape_position = [(0, 4)]

        while True:
            print_grid(grid, len(SHAPES) + 1, shape_position)
            time.sleep(0.3)

            new_shape_position = [(x + 1, y) for x, y in shape_position]
            if not check_collision(grid, current_shape, new_shape_position):
                shape_position = new_shape_position
            else:
                merge_shape(grid, current_shape, shape_position, len(SHAPES) + 1)
                remove_completed_lines(grid)
                break

        if check_collision(grid, current_shape, shape_position):
            print("Game Over!")
            break

    print("Your score:", score)

if __name__ == "__main__":
    main()