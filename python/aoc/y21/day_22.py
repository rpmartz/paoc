def parse_range(range_notation):
    """
    parses a range notation like x=10..12 to a start and stop, (10, 13) in this case
    """

    start_and_stop_with_dots = range_notation.split('=')
    numbers = start_and_stop_with_dots[1].split('..')

    return int(numbers[0]), int(numbers[1])


def cuboid_from_line(line):
    direction, rest = line.split(' ')

    ranges = line.split(',')
    x_start, x_stop = parse_range(ranges[0])
    y_start, y_stop = parse_range(ranges[1])
    z_start, z_stop = parse_range(ranges[2])

    cuboids = set()

    for x in range(max(x_start, -50), min(50, x_stop) + 1):
        for y in range(max(y_start, -50), min(50, y_stop) + 1):
            for z in range(max(z_start, -50), min(50, z_stop) + 1):
                cuboids.add((x, y, z))

    return direction, cuboids


def process(lines):
    state = {
        'on': set(),
        'off': set(),
    }

    for line in lines:
        direction, cuboids = cuboid_from_line(line)
        if direction == 'on':
            off_cuboids = state['off']
            on_cuboids = state['on']
            for cuboid in cuboids:
                on_cuboids.add(cuboid)
                if cuboid in off_cuboids:
                    off_cuboids.remove(cuboid)

            state['on'] = on_cuboids
            state['off'] = off_cuboids

        else:
            off_cuboids = state['off']
            on_cuboids = state['on']
            for cuboid in cuboids:
                if cuboid in on_cuboids:
                    on_cuboids.remove(cuboid)
                off_cuboids.add(cuboid)

            state['on'] = on_cuboids
            state['off'] = off_cuboids

    return state


if __name__ == '__main__':
    with open('data/day22.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    result = process(lines)
    print(len(result['on']))
