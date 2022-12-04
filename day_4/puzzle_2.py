def range_contains(pair: str) -> bool:
    elf_1, elf_2 = pair.split(',')
    elf_1_section_min, elf_1_section_max = elf_1.split('-')
    elf_2_section_min, elf_2_section_max = elf_2.split('-')
    return int(elf_1_section_min) > int(elf_2_section_max) or int(elf_2_section_min) > int(elf_1_section_max)


if __name__ == '__main__':
    counter = 0
    with open('day_4_input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            if range_contains(line):
                counter += 1

    # Find all rows that don't overlap at all and minus from total rows
    print(len(lines) - counter)
