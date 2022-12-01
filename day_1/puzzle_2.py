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


def calculate_top_three_calories(elves):
    total_calories = 0
    sum_elves_cals = dict(enumerate(map(sum, elves)))
    for i in range(3):
        index = max(sum_elves_cals, key=lambda n: sum_elves_cals[n])
        total_calories += sum_elves_cals.pop(index)

    return total_calories


if __name__ == '__main__':
    elves = parse_input('day_1_input.txt')
    print(calculate_top_three_calories(elves))
