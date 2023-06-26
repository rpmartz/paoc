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

    # horizontal segment means `x` coords change, `y` for vertical
    i = 0 if is_horizontal else 1

    # direction to move
    step = 1 if end[i] > start[i] else -1

    for coord in range(start[i], end[i] + step, step):
        if is_horizontal:
            included_points.append((coord, start[i]))
        else:
            included_points.append((start[i], coord))


    return included_points


