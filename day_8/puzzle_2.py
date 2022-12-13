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


def get_scenic_score(val: int, direction_array: np.ndarray) -> int:
    counter = 0
    for tree in direction_array:
        counter += 1
        if val <= tree:
            break
    return counter


def get_highest_scenic_score(forest: np.ndarray) -> int:
    highest_score = 0
    highest_tree = ()
    for idx, x in np.ndenumerate(forest):
        # Check left
        left = get_scenic_score(x, np.flip(forest[idx[0], :idx[1]]))
        # Check right
        right = get_scenic_score(x, forest[idx[0], idx[1]+1:])
        # Check up
        up = get_scenic_score(x, np.flip(forest[:idx[0], idx[1]]))
        # Check down
        down = get_scenic_score(x, forest[idx[0]+1:, idx[1]])

        total_scenic_score = left * right * up * down
        if total_scenic_score > highest_score:
            highest_score = total_scenic_score

    return highest_score


if __name__ == '__main__':
    input_forest = parse_input('day_8_input.txt')
    score = get_highest_scenic_score(input_forest)
    print(score)
