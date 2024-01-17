import re
from collections import defaultdict
from itertools import permutations

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

    all_paths = permutations(dists.keys())

    shortest = 99999999999
    longest = -99999999999

    for path in all_paths:
        path_distance = 0
        for src, dest in zip(path, path[1:]):
            path_distance += dists[src][dest]

        shortest = min(shortest, path_distance)
        longest = max(longest, path_distance)

    print(f"Part 1: {shortest}")
    print(f"Part 2: {longest}")
