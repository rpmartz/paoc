from collections import namedtuple

Point3D = namedtuple('Point3D', 'x y z')
Point = namedtuple('Point', 'x, y')


def manhattan_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
