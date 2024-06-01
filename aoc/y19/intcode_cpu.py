

ADD = 1
MULTIPLY = 2
HALT = 99
def execute_instructions(instructions):
    pc = 0
    while pc < len(instructions):
        opcode = instructions[pc]

        op1 = instructions[instructions[pc + 1]]
        op2 = instructions[instructions[pc + 2]]
        destination = instructions[pc + 3]

        if opcode == ADD:
            instructions[destination] = op1 + op2
        elif opcode == MULTIPLY:
            instructions[destination] = op1 * op2
        elif opcode == HALT:
            return instructions
        else:
            raise Exception(f"Unknown opcode {opcode}")

        pc += 4

    return instructions
