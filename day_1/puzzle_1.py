def parse_input(file):
    elves = []
    with open(file) as f:
        elf = []
        line = f.readline()
        while line:
            if line == '\n':
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line.rstrip('\n')))
            line = f.readline()

    return elves


def calculate_max_calories(elves):
    return max(map(sum, elves))


if __name__ == '__main__':
    elves = parse_input('day_1_input.txt')
    print(calculate_max_calories(elves))
