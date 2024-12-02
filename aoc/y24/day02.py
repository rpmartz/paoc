from aoc.common.parsing import ints

def get_lines():
    with open('data/day02.txt', 'r') as f:
        lines = [ints(l.strip()) for l in f.readlines()]

    return lines

# for line in get_lines():
