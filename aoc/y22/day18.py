from aoc.common.geometry import Point3D

dirs = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (-1, 0, 0), (0, -1, 0), (0, 0, -1),
]

cubic_neighbors = [(0, 0, 1), (0, 0, -1),
                   (0, 1, 0), (0, -1, 0),
                   (1, 0, 0), (-1, 0, 0)
                   ]


def get_neighbors(p: Point3D):
    neighbors = set()
    for vec in cubic_neighbors:
        x = p.x + vec[0]
        y = p.y + vec[1]
        z = p.z + vec[2]
        neighbors.add(Point3D(x, y, z))

    return neighbors
