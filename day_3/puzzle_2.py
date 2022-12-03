def char_to_priority(char: str) -> int:
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def parse_input(file_path: str) -> list[list[str]]:
    with open(file_path) as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines), 3):
            yield lines[i:i+3]


def get_common_item_type(rucksacks) -> str:
    common_item_type_set = set(rucksacks[0])
    for i in range(1, len(rucksacks)):
        common_item_type_set = common_item_type_set.intersection(rucksacks[i])
    return ''.join(common_item_type_set)


if __name__ == '__main__':
    groups = parse_input('day_3_input.txt')
    total_priority = sum([char_to_priority(get_common_item_type(rucksacks)) for rucksacks in groups])
    print(total_priority)
