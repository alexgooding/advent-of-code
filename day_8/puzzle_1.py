import numpy as np


def parse_input(file_path: str) -> np.ndarray:
    with open(file_path) as f:
        matrix = []
        while True:
            line = f.readline().strip()
            if line:
                matrix.append([int(c) for c in line])
            else:
                break

        return np.array(matrix)


def check_visibility(val: int, direction_array: np.ndarray) -> bool:
    for tree in direction_array:
        if val <= tree:
            return False
    return True


def count_visible_trees(forest: np.ndarray) -> int:
    counter = 0
    for idx, x in np.ndenumerate(forest):
        # Check edge
        if idx[0] == 0 or idx[1] == 0:
            counter += 1
        # Check left
        elif check_visibility(x, forest[idx[0], :idx[1]]):
            counter += 1
        # Check right
        elif check_visibility(x, forest[idx[0], idx[1]+1:]):
            counter += 1
        # Check up
        elif check_visibility(x, forest[:idx[0], idx[1]]):
            counter += 1
        # Check down
        elif check_visibility(x, forest[idx[0]+1:, idx[1]]):
            counter += 1

    return counter


if __name__ == '__main__':
    input_forest = parse_input('day_8_input.txt')
    visible_tree_count = count_visible_trees(input_forest)
    print(visible_tree_count)
