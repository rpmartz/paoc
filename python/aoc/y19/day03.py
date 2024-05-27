
DIRECTIONS = {
    'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)
}

def read_lines():
    with open("inputs/day03.txt") as f:
        return [l.strip() for l in f.readlines()]

def trace_wire_path(movements):
    visited = {}

    x = 0
    y = 0
    num_steps = 0

    for movement in movements:
        direction = movement[0]
        distance = int(movement[1:])

        for _ in range(distance):
            dx, dy = DIRECTIONS[direction]

            x += dx
            y += dy
            num_steps += 1

            visited.setdefault((x, y), num_steps)

    return visited

lines = read_lines()

w1 = trace_wire_path(lines[0].split(','))
w2 = trace_wire_path(lines[1].split(','))

intersections = set(w1) & set(w2)

print(min(w1[i] + w2[i] for i in intersections))