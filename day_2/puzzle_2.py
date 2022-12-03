POINT_COMBINATIONS = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
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
