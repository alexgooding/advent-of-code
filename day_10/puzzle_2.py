def parse_input(file_path: str) -> list:
    with open(file_path) as f:
        output = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            if line == 'noop':
                output.append(0)
            else:
                output.append(int(line.split()[1]))

        return output


def get_pixel_type(cycle: int, sprite_position: int) -> str:
    if cycle in [sprite_position - 1, sprite_position, sprite_position + 1]:
        return '#'
    else:
        return '.'


def print_crt(input_sequence: list):
    cycle = 0
    sprite_position = 1
    for elem in input_sequence:
        if elem == 0:
            n = 1
        else:
            n = 2
        for i in range(n):
            pixel = get_pixel_type(cycle, sprite_position)
            if cycle >= 39:
                cycle = 0
                print(pixel)
            else:
                print(pixel, end=' ')
                cycle += 1
        sprite_position += elem


if __name__ == '__main__':
    sequence = parse_input('day_10_input.txt')
    print_crt(sequence)
