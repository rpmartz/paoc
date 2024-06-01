from aoc.common.parsing import split_and_parse
from intcode_cpu import execute_instructions
def read_input() -> list[int]:
    with open('inputs/day02.txt', 'r') as f:
        opcodes = f.read()

    return split_and_parse(opcodes)

instructions = read_input()
instructions[1] = 12
instructions[2] = 2
result = execute_instructions(instructions)

print(result[0])
