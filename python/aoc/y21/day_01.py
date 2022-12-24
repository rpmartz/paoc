def read_file():
    with open('data/day01.txt', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def do_part_one():
    lines = read_file()
    num_increases = sum(a < b for a, b in zip(lines, lines[1:]))

    print('Number of times sonar depth reading increased: %d' % num_increases)


def do_part_two():
    lines = read_file()

    windows = [sum(lines[i:i + 3]) for i in range(len(lines) - 2)]
    num_increases = sum(a < b for a, b in zip(windows, windows[1:]))

    print('%d sliding windows have increasing sums' % num_increases)


if __name__ == '__main__':
    do_part_one()
    do_part_two()
