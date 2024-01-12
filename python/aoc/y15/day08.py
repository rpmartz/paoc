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
            if next_char in {'"', '\\'}:
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


def encode_line(line):
    cursor = 0
    encoded_chars = ['"']
    while cursor < len(line):
        char = line[cursor]
        if char in {'"', '\\'}:
            encoded_chars.append("\\")

        encoded_chars.append(char)
        cursor += 1

    encoded_chars.append('"')
    return ''.join(encoded_chars)

if __name__ == '__main__':
    lines = read_lines()

    original_chars = 0
    encoded_chars = 0
    for line in lines:
        original_chars += len(line)
        encoded_chars += len(encode_line(line))

    difference = encoded_chars - original_chars
    print(difference)
