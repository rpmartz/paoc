import ast
from collections import namedtuple

Packet = namedtuple('Packet', 'left, right')


def get_input():
    with open('data/day13.txt', 'r') as f:
        lines = f.read()
    return lines


def parse_input(lines):
    groups = lines.split('\n\n')

    packets = []
    for group in groups:
        elems = group.split('\n')
        assert len(elems) == 2
        packets.append(Packet(ast.literal_eval(elems[0]), ast.literal_eval(elems[1])))

    return packets


def compare_packet(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, int):
        return compare_packet(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare_packet([left], right)
    else:
        for left_el, right_el in zip(left, right):
            if left_el != right_el:
                return compare_packet(left_el, right_el)

        return compare_packet(len(left), len(right))


def part_one():
    lines = get_input()
    packets = parse_input(lines)
    correct_packet_indicies = []
    for idx, el in enumerate(packets):
        if compare_packet(el.left, el.right) < 0:
            correct_packet_indicies.append(idx + 1)

    return sum(correct_packet_indicies)


if __name__ == '__main__':
    print(f'part 1: {part_one()}')
