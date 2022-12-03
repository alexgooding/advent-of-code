POINT_COMBINATIONS = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}


def parse_input(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.read().splitlines()


def calculate_round_score(pair: str) -> int:
    return POINT_COMBINATIONS[pair]


if __name__ == '__main__':
    guide = parse_input('day_2_input.txt')
    total = sum(map(calculate_round_score, guide))
    print(total)
