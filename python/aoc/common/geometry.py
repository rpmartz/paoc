from collections import namedtuple
from dataclasses import dataclass

Point3D = namedtuple('Point3D', 'x y z')

@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    # TODO best way to declare this? https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
    def manhattan_distance_to(self, p: 'Point') -> int:
        return manhattan_distance(self, p)

def manhattan_distance(p1: Point, p2: Point):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
