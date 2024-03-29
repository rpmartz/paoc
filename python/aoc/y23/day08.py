from itertools import cycle
import re
from collections import defaultdict
from math import lcm

def read_lines():
    with open("data/day08.txt") as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def part_one(node_mappings, instructions):
    current_node = "AAA"
    steps = 0

    for instr in cycle(instructions):
        node = node_mappings[current_node]
        steps += 1

        if instr == "L":
            current_node = node[0]
        elif instr == "R":
            current_node = node[1]

        if current_node == "ZZZ":
            break

    print(steps)


def part_two(node_mappings, instructions):
    a_nodes = {k: k for k in node_mappings.keys() if k.endswith("A")}
    steps = 0

    step_counts = defaultdict(int)

    for instr in cycle(instructions):

        steps += 1

        for a_node, current_location in a_nodes.items():

            node = node_mappings[current_location]

            if current_location.endswith("Z"):
                continue

            if instr == "L":
                current_node = node[0]
            elif instr == "R":
                current_node = node[1]

            a_nodes[a_node] = current_node

            if current_node.endswith("Z") and a_node not in step_counts.keys():
                step_counts[a_node] = steps

        if all([v.endswith("Z") for v in a_nodes.values()]):
            break

    print(lcm(*step_counts.values()))


if __name__ == "__main__":

    lines = read_lines()
    instructions = lines[0]
    mappings = lines[2:]

    nodes = {}
    for line in mappings:
        node, left, right = re.findall(r"\w+", line)
        nodes[node] = (left, right)

    part_one(nodes, instructions)
    part_two(nodes, instructions)
