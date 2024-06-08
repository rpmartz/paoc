
def read_instructions():
    with open('inputs/day05.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    instructions = [int(i) for i in lines[0].split(',')]
    return instructions

print(read_instructions())