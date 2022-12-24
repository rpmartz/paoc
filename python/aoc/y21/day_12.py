from collections import defaultdict

test_input = """\
start-qs
qs-jz
start-lm
qb-QV
QV-dr
QV-end
ni-qb
VH-jz
qs-lm
qb-end
dr-fu
jz-lm
start-VH
QV-jz
VH-qs
lm-dr
dr-ni
ni-jz
lm-QV
jz-dr
ni-end
VH-dr
VH-ni
qb-HE
"""


def calculate_paths(input):
    paths = defaultdict(set)

    for path in input.splitlines():
        source, destination = path.split('-')

        # graph is bidrectional so a-b means path from a to b and b to a
        paths[source].add(destination)
        paths[destination].add(source)

    all_paths = set()
    nodes_to_process = [(('start',), False)]
    while nodes_to_process:
        path, small_cave_visited_twice = nodes_to_process.pop()

        if path[-1] == 'end':
            all_paths.add(path)
            continue

        for node in paths[path[-1]]:  # get all of the nodes that the last node in the current path has a connection to
            if node == 'start':
                continue
            elif node.isupper() or node not in path:
                nodes_to_process.append(((*path, node), small_cave_visited_twice))
            elif not small_cave_visited_twice and path.count(node) == 1:
                nodes_to_process.append(((*path, node), True))

    return len(all_paths)


print(calculate_paths(test_input))
