def parse_input(file_path: str) -> str:
    with open(file_path) as f:
        return f.readline()


def get_marker_location(s: str) -> int:
    counter = 0
    previous_chars = []
    for c in s:
        if c in previous_chars:
            previous_chars = previous_chars[previous_chars.index(c)+1:]
        previous_chars.append(c)
        counter += 1
        if len(previous_chars) == 4:
            break

    return counter


if __name__ == '__main__':
    datastream = parse_input('day_6_input.txt')
    number_of_chars_processed = get_marker_location(datastream)
    print(number_of_chars_processed)
