def parse_input(file_path: str) -> tuple[dict[int, list[str]], list[tuple[int, int, int]]]:
    with open(file_path) as f:
        stacks = dict()
        instructions = []
        lines = f.readlines()
        # construct stacks
        while lines:
            line = lines.pop(0)
            if line == '\n':
                break
            elif line[1].isdigit():
                continue
            else:
                for i in range(0, len(line), 4):
                    if line[i] == '[':
                        stacks.setdefault(int((i+4)/4), []).insert(0, line[i+1])

        # construct instructions
        while lines:
            line = lines.pop(0)
            split_str = line.split()
            instructions.append((int(split_str[1]), int(split_str[3]), int(split_str[5])))

        return stacks, instructions


def move_crates(stacks, instructions):
    for move in instructions:
        for i in range(move[0]):
            stacks.setdefault(move[2], []).append(stacks[move[1]].pop())

    return stacks


def get_top_crates(stacks):
    top_crates = ''
    for i in range(1, len(stacks)+1):
        top_crates += stacks[i][-1]

    return top_crates


if __name__ == '__main__':
    stacks, instructions = parse_input('day_5_input.txt')
    stacks = move_crates(stacks, instructions)
    top_crates = get_top_crates(stacks)
    print(top_crates)
