from itertools import cycle
import re

def read_lines():
    with open('data/day08.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines



lines = read_lines()
instructions = lines[0]
mappings = lines[2:]

nodes = {}
for line in mappings:
    node, left, right = re.findall(r'\w+', line)
    nodes[node] = (left, right)

print(nodes)

current_node = 'AAA'
steps = 0

for instr in cycle(instructions):
    node = nodes[current_node]
    steps += 1

    if instr == 'L':
        current_node = node[0]
    elif instr == 'R':
        current_node = node[1]
    else:
        raise ValueError(f'Unknown instruction: {instr}')

    if current_node == 'ZZZ':
        break

print(steps)




