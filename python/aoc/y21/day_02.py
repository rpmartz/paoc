def read_file():
    with open('data/day02.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def part_one(lines):
    x = 0
    y = 0
    for line in lines:
        components = line.split(' ')
        direction = components[0]
        magnitude = int(components[1])

        if direction == 'forward':
            x = x + magnitude
        elif direction == 'up':
            y = y - magnitude
        elif direction == 'down':
            y = y + magnitude

    print('End position is %s, %s' % (x, y))
    print('Product of end position is %d' % (x * y))


def part_two(lines):
    print('\n\n=== part two ===\n\n')
    horizontal_pos = 0
    depth = 0
    aim = 0

    for line in lines:
        components = line.split(' ')
        direction = components[0]
        magnitude = int(components[1])

        if direction == 'forward':
            horizontal_pos = horizontal_pos + magnitude
            depth = depth + (aim * magnitude)
        elif direction == 'up':
            aim = aim - magnitude
        elif direction == 'down':
            aim = aim + magnitude

    print('End position is horizontal_pos: %s, depth: %s aim: %s' % (horizontal_pos, depth, aim))
    print('Product of end position is %d' % (horizontal_pos * depth))


if __name__ == '__main__':
    lines = read_file()
    part_one(lines)
    part_two(lines)
