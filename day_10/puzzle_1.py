def parse_input(file_path: str) -> list:
    with open(file_path) as f:
        output = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            if line == 'noop':
                output.append('')
            else:
                output.append(int(line.split()[1]))

        return output


def calculate_sum_of_signal_strengths(input_sequence: list) -> int:
    signal_strengths_at_20 = {}
    cycle = 0
    x = 1
    for elem in input_sequence:
        if elem == '':
            cycle += 1
            if cycle % 20 == 0:
                signal_strengths_at_20[cycle] = cycle * x
        else:
            cycle += 2
            if cycle % 20 in [0, 1]:
                signal_strengths_at_20[(cycle // 10) * 10] = ((cycle // 10) * 10 * x)
                x += elem
            else:
                x += elem

    return signal_strengths_at_20[20] + signal_strengths_at_20[60] + signal_strengths_at_20[100] + \
           signal_strengths_at_20[140] + signal_strengths_at_20[180] + signal_strengths_at_20[220]


if __name__ == '__main__':
    sequence = parse_input('day_10_input.txt')
    result = calculate_sum_of_signal_strengths(sequence)
    print(result)
