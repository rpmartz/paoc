

with open('data/day24.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

results = []
for line in lines:
    if line == 'inp w':
        results.append(line)
        continue

    components = line.split(' ')
    instruction = components[0]
    first = components[1]
    second = components[2]

    operand = None
    if instruction == 'mul':
        results.append(f'{first.upper()} = {first.upper()} * {second.upper()}; // {line}')
    elif instruction == 'add':
        results.append(f'{first.upper()} = {first.upper()} + {second.upper()}; // {line}')
    elif instruction == 'div':
        results.append(f'{first.upper()} = {first.upper()} / {second.upper()}; // {line}')
    elif instruction == 'mod':
        results.append(f'{first.upper()} = {first.upper()} % {second.upper()}; // {line}')
    elif instruction == 'eql':
        results.append(f'{first.upper()} = {first.upper()} == {second.upper()} ? 1 : 0; // {line}')
    else:
        raise Exception(f'Should never get here. Line [{line}]')

for r in results:
    print(r)
