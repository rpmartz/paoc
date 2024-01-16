import re
from collections import defaultdict
import pprint

# input is an undirected weighted graph
def load_graph():
    distances = defaultdict(dict)

    with open("data/day09.txt", "r") as ifile:
        lines = [l.strip() for l in ifile.readlines()]

    for line in lines:
        result = re.match("(\w+) to (\w+) = (\d+)", line)
        src, dest, dist = result.groups()

        distances[src][dest] = int(dist)
        distances[dest][src] = int(dist)

    return distances


def load_edges():
    with open("data/day09.txt", "r") as ifile:
        lines = [l.strip() for l in ifile.readlines()]

    edges = []

    for line in lines:
        result = re.match("(\w+) to (\w+) = (\d+)", line)
        src, dest, dist = result.groups()

        edges.append((int(dist), src, dest))

    return edges


if __name__ == "__main__":
    dists = load_graph()
    edges = sorted(load_edges())

    visited = set()
    distance_traveled = 0

    # start randomly at Faerun
    visited.add("Faerun")

    while len(visited) < len(dists.keys()) - 1:
        for dist, src, dest in edges:
            if src not in visited and dest in visited:
                print(f"\tAdding edge {src} - {dest} of cost {dist}")
                visited.add(src)
                distance_traveled += dist
            elif src in visited and dest not in visited:
                print(f"\tAdding edge {src} - {dest} of cost {dist}")
                visited.add(dest)
                distance_traveled += dist

    print(sorted(visited))
    print(distance_traveled)
