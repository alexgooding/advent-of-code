from collections import namedtuple

Motion = namedtuple('Motion', 'direction distance')
Point = namedtuple('Point', 'x y')


def parse_input(file_path: str) -> list[namedtuple]:
    with open(file_path) as f:
        output = []
        while True:
            line = f.readline().strip()
            if line:
                split_line = line.split()
                output.append(Motion(split_line[0], int(split_line[1])))
            else:
                break

        return output


def head_movement(point: Point, direction: str) -> Point:
    if direction == 'L':
        point = Point(point.x - 1, point.y)
    elif direction == 'R':
        point = Point(point.x + 1, point.y)
    elif direction == 'U':
        point = Point(point.x, point.y + 1)
    elif direction == 'D':
        point = Point(point.x, point.y - 1)

    return point


def tail_movement(tail_point: Point, head_point: Point) -> Point:
    if abs(tail_point.x - head_point.x) <= 1 and abs(tail_point.y - head_point.y) <= 1:
        return tail_point

    if tail_point.x == head_point.x:
        # Move vertically
        if tail_point.y < head_point.y:
            tail_point = Point(tail_point.x, tail_point.y + 1)
        else:
            tail_point = Point(tail_point.x, tail_point.y - 1)
    elif tail_point.y == head_point.y:
        # Move horizontally
        if tail_point.x < head_point.x:
            tail_point = Point(tail_point.x + 1, tail_point.y)
        else:
            tail_point = Point(tail_point.x - 1, tail_point.y)
    else:
        # Move diagonally
        if tail_point.x < head_point.x and tail_point.y < head_point.y:
            tail_point = Point(tail_point.x + 1, tail_point.y + 1)
        elif tail_point.x < head_point.x and tail_point.y > head_point.y:
            tail_point = Point(tail_point.x + 1, tail_point.y - 1)
        elif tail_point.x > head_point.x and tail_point.y < head_point.y:
            tail_point = Point(tail_point.x - 1, tail_point.y + 1)
        else:
            tail_point = Point(tail_point.x - 1, tail_point.y - 1)

    return tail_point


def perform_motions(motions: list[Motion]) -> int:
    head_point = Point(0, 0)
    tail_points = 9 * [Point(0, 0)]
    visited_points = []
    for motion in motions:
        for i in range(motion.distance):
            head_point = head_movement(head_point, motion.direction)
            head_iteration = head_point
            for j in range(len(tail_points)):
                tail_points[j] = tail_movement(tail_points[j], head_iteration)
                head_iteration = tail_points[j]
            visited_points.append(tail_points[-1])

    return len(set(visited_points))


if __name__ == '__main__':
    motions_list = parse_input('day_9_input.txt')
    number_of_positions = perform_motions(motions_list)
    print(number_of_positions)
