from python.aoc.common.parsing import ints

def get_instructions():
    with open('data/day06.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    instructions = []
    for line in lines:
         coords = ints(line)
         if 'off' in line:
             instructions.append(('off', (coords[0], coords[1]),(coords[2], coords[3])))
         elif 'on' in line:
             instructions.append(('on', (coords[0], coords[1]), (coords[2], coords[3])))
         else:
             instructions.append(('toggle', (coords[0], coords[1]), (coords[2], coords[3])))

    return instructions

print(get_instructions())