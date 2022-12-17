from collections import namedtuple

Point2D = namedtuple('Point', 'x y')


def read_numeric_grid(inp: str) -> dict[Point2D, int]:
    grid = {}
    for x, line in enumerate(inp.splitlines()):
        for y, digit in enumerate(line.strip()):
            grid[(x, y)] = int(digit)

    return grid


def get_neighbors(point: Point2D, num=4) -> set[Point2D]:
    """
    Gets the neighbors for a point. Assumes that the caller will perform bounds checking, i.e.
    given the point 0, 0 it will return negative valued number for points.

    :param point: the point whose neighbors you want
    :param num: the number of points to get, either 4 (left, right, top, bottom) or 8 (includes diagonals)
    :return: neighbors of the point in a set
    """
    if num not in {4, 8}:
        raise Exception(f'Invalid argument {num}. Can get 4 or 8 neighbors')

    if num == 4:
        return {Point2D(x=point.x + 1, y=point.y), Point2D(x=point.x - 1, y=point.y), Point2D(x=point.x, y=point.y + 1),
                Point2D(x=point.x, y=point.y - 1)}
    else:
        neighbors = set()
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue

                neighbors.add(Point2D(point.x + x, point.y + y))

        return neighbors
