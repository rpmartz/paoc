from python.aoc.common.geometry import Point3D

cubic_neighbor_directions = [(0, 0, 1), (0, 0, -1),
                             (0, 1, 0), (0, -1, 0),
                             (1, 0, 0), (-1, 0, 0)]


def get_neighbors(p: Point3D):
    neighbors = set()
    for vec in cubic_neighbor_directions:
        x = p.x + vec[0]
        y = p.y + vec[1]
        z = p.z + vec[2]
        neighbors.add(Point3D(x, y, z))

    return neighbors


def get_input():
    with open('data/day18.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def parse_lines(lines):
    points = set()
    for line in lines:
        x, y, z = line.split(',')
        points.add(Point3D(int(x), int(y), int(z)))

    return points


points = parse_lines(get_input())

num_sides = 6
total_area = 0

for point in points:
    neighbors = get_neighbors(point)

    num_covered_sides = 0
    for neighbor in neighbors:
        if neighbor in points:
            num_covered_sides += 1

    num_uncovered_sides = num_sides - num_covered_sides
    total_area += num_uncovered_sides

print(total_area)
