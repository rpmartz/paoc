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
        lhs, rhs = line.split(' -> ')
        table[rhs] = lhs

    return table


def charge(wire, wire_values) -> int:
    if wire.isnumeric():
        return int(wire)

    rhs = wire_values[wire]
    print(f'{wire} -> {rhs}')

    if isinstance(rhs, int):
        wire_values[wire] = rhs
        return wire_values[wire]
    elif ' ' not in rhs:
        res = charge(rhs, wire_values)
        wire_values[wire] = res
        return res
    elif rhs.startswith('NOT'):
        res = ~charge(rhs.replace('NOT ', ''), wire_values) & 0xffff
        wire_values[wire] = res
        return res
    else:
        l, op, r = rhs.split(' ')
        operation = operators[op]
        res = operation(charge(l, wire_values), charge(r, wire_values))
        wire_values[wire] = res

        return res


if __name__ == '__main__':
    lines = read_lines()
    stable = symbol_table(lines)

    res = charge('a', stable)
    print(res)
