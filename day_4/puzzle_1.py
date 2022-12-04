def range_contains(pair: str) -> bool:
    elf_1, elf_2 = pair.split(',')
    elf_1_section_min, elf_1_section_max = elf_1.split('-')
    elf_2_section_min, elf_2_section_max = elf_2.split('-')
    return (int(elf_1_section_min) <= int(elf_2_section_min) and int(elf_2_section_max) <= int(elf_1_section_max)) or \
           (int(elf_2_section_min) <= int(elf_1_section_min) and int(elf_1_section_max) <= int(elf_2_section_max))


if __name__ == '__main__':
    result = 0
    with open('day_4_input.txt') as f:
        line = f.readline().rstrip('\n')
        while line:
            if range_contains(line):
                result += 1
            line = f.readline()

    print(result)
