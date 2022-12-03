def char_to_priority(char: str) -> int:
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def parse_input(file_path: str) -> list[list[str]]:
    with open(file_path) as f:
        return [[line[:len(line)//2], line[len(line)//2:]] for line in f.read().splitlines()]


def get_common_item_type(rucksack: list[str]) -> str:
    return ''.join(set(rucksack[0]).intersection(rucksack[1]))


if __name__ == '__main__':
    rucksacks = parse_input('day_3_input.txt')
    total_priority = sum([char_to_priority(get_common_item_type(rucksack)) for rucksack in rucksacks])
    print(total_priority)
