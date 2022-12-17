from collections import namedtuple

Move = namedtuple('Move', 'dir steps')


def get_input():
    with open('data/day09.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def parse_moves(input):
    moves = []
    for inst in input:
        components = inst.split(' ')
        moves.append(Move(dir=components[0], steps=int(components[1])))

    return moves


print(parse_moves(get_input()))
