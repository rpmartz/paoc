NON_MEM_CHARS = {'"', '\\'}


def read_lines():
    with open('data/day08.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def determine_mem_chars(line):
    mem_chars = 0
    cursor = 0

    while cursor < len(line):
        char = line[cursor]
        if char == '"':
            cursor += 1
        elif char == '\\':
            next_char = line[cursor + 1]
            if next_char == '"':
                cursor += 2
                mem_chars += 1
            elif next_char == '\\':
                cursor += 2
                mem_chars += 1
            elif next_char == 'x':
                cursor += 4
                mem_chars += 1
            else:
                raise Exception(f'Unknown next_char: {next_char}')

        else:
            mem_chars += 1
            cursor += 1

    return mem_chars


if __name__ == '__main__':
    lines = read_lines()

    code_chars = 0
    mem_chars = 0
    for line in lines:
        code_chars += len(line)
        mem_chars += determine_mem_chars(line)

    difference = code_chars - mem_chars
    print(difference)
