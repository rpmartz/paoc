import re
from collections import defaultdict
import pprint
# input is a bidirectional weighted graph
def load_graph():
    distances = defaultdict(dict)

    with open("data/day09.txt", "r") as ifile:
        lines = [l.strip() for l in ifile.readlines()]

    for line in lines:
        result = re.match("(\w+) to (\w+) = (\d+)", line)
        src, dest, dist = result.groups()

        distances[src][dest] = int(dist)


    return distances

if __name__ == '__main__':
    dists = load_graph()


