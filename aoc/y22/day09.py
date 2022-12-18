from collections import namedtuple

Move = namedtuple('Move', 'dir steps')
Point = namedtuple('Point', 'x y')


def signum(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


def get_input():
    with open('data/day09.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def parse_moves(inp):
    moves = []
    for inst in inp:
        components = inst.split(' ')
        moves.append(Move(dir=components[0], steps=int(components[1])))

    return moves


def build_rope(num_knots):
    return [Point(x=0, y=0) for _ in range(num_knots)]


def move_head(head, move):
    for _ in range(move.steps):
        if move.dir == 'R':
            return Point(head.x + 1, head.y)
        elif move.dir == 'L':
            return Point(head.x - 1, head.y)
        elif move.dir == 'U':
            return Point(head.x, head.y + 1)
        elif move.dir == 'D':
            return Point(head.x, head.y - 1)


def follow(first: Point, second: Point) -> Point:
    dx, dy = first.x - second.x, first.y - second.y
    if abs(dx) < 2 and abs(dy) < 2:
        return second
    else:
        x_delta = signum(dx)
        y_delta = signum(dy)

        return Point(second.x + x_delta, second.y + y_delta)


def run(moves, num_knots):
    rope = build_rope(num_knots)
    visited = set(rope[-1])

    for move in moves:
        for step in range(move.steps):
            rope[0] = move_head(rope[0], move)
            for knot in range(1, len(rope)):
                rope[knot] = follow(rope[knot - 1], rope[knot])

            visited.add(rope[-1])

    return visited


# todo: off by one here somehwere compared to clojure version
moves = parse_moves(get_input())
all_visited = run(moves, 10)
print(len(all_visited))
