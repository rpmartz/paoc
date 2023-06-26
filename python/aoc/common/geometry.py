from collections import namedtuple
from dataclasses import dataclass
from typing import Tuple, Union, Set, List

Point3D = namedtuple('Point3D', 'x y z')

@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    # TODO best way to declare this? https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
    def manhattan_distance_to(self, p: 'Point') -> int:
        return manhattan_distance(self, p)

    def as_tuple(self) -> Tuple:
        return (self.x, self.y)

def manhattan_distance(p1: Union[Point | Tuple], p2: Union[Point | Tuple]):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def points_between_inclusive(start: Tuple, end: Tuple) -> List[Tuple]:
    """
    Takes two 2d points and returns all the points in between them. Returns a list
    rather than a set to preserve order, in case it's used in the case of
    "first encountered" problems.
    """

    is_vertical = start[0] == end[0]
    is_horizontal = start[1] == end[1]

    assert is_horizontal or is_vertical, "x or y coordinates of the points must match"

    included_points = []

    if is_horizontal:
        if end[0] > start[0]:
            step = 1
        else:
            step = -1

        for x in range(start[0], end[0] + step, step):
            included_points.append((x, start[1]))

    else:
        if end[1] > start[1]:
            step = 1
        else:
            step = -1

        for y in range(start[1], end[1] + step, step):
            included_points.append((start[0], y))

    return included_points


