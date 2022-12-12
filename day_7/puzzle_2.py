SPACE_REQUIRED = 8381165


class Dir:
    def __init__(self, name, parent_dir=None, total_subdir_size=0, total_file_size=0):
        self.name = name
        self.total_subdir_size = total_subdir_size
        self.parent_dir = parent_dir
        self.total_file_size = total_file_size

    def calculate_size(self):
        return self.total_subdir_size + self.total_file_size


def parse_input(file_path: str) -> list[list[str]]:
    with open(file_path) as f:
        return [line.split() for line in f.readlines()]


def map_file_system(input):
    total_sizes = []
    current_dir = None
    for line in input:
        if line == ['$', 'cd', '..']:
            dir_size = current_dir.calculate_size()
            if dir_size >= SPACE_REQUIRED:
                total_sizes.append(dir_size)
            current_dir = current_dir.parent_dir
            current_dir.total_subdir_size += dir_size
        elif line[0] == '$' and line[1] == 'cd':
            current_dir = Dir(line[2], current_dir)
        elif line[0].isdigit():
            current_dir.total_file_size += int(line[0])

    return total_sizes


if __name__ == '__main__':
    terminal_output = parse_input('day_7_input.txt')
    required_sizes = map_file_system(terminal_output)
    required_sizes.sort()
    print(required_sizes[0])
