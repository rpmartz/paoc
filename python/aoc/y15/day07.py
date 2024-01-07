import operator

operators = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
}
def read_lines():
    with open('data/day07.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines

def symbol_table(lines):
    table = {}
    for line in lines:
        print(line)
        lhs, rhs = line.split(' -> ')
        print(f'\t{rhs} = {lhs}')
        table[rhs] = lhs

    return table

def determine_signal(wire_name, table):
    if wire_name.isnumeric():
        return int(wire_name)

    val = table[wire_name]

    if val.startswith('NOT'):
        return ~determine_signal(table[val.split(" ")[1]], table)
    elif ' ' not in val:
        return determine_signal(val, table)
    else:
        lhs, op, rhs = val.split(' ')

        operation = operators[op]
        return operation(determine_signal(lhs, table), determine_signal(rhs, table))

if __name__ == '__main__':
    lines = read_lines()
    stable = symbol_table(lines)
    print(determine_signal('a', stable))

