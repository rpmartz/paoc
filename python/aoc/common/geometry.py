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

def points_between_inclusive(p1: Tuple, p2: Tuple) -> List[Tuple]:
    """
    Takes two 2d points and returns all the points in between them. Returns a list
    rather than a set to preserve order, in case it's used in the case of
    "first encountered" problems.
    """

    is_vertical = p1[0] == p2[0]
    is_horizontal = p1[1] == p2[1]

    assert is_horizontal or is_vertical, "x or y coordinates of the points must match"

    included_points = []

    if is_horizontal:
        start = min(p1[0], p2[0])
        end = max(p1[0], p2[0])
        for x in range(start, end + 1):
            included_points.append((x, p1[1]))

    else:
        start = min(p1[1], p2[1])
        end = max(p1[1], p2[1])
        for y in range(start, end + 1):
            included_points.append((p1[0], y))

    return included_points


