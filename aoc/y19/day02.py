from aoc.common.parsing import split_and_parse
def read_input() -> list[int]:
    with open('inputs/day02.txt', 'r') as f:
        opcodes = f.read()

    return split_and_parse(opcodes)

print(read_input())

