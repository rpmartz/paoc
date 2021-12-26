if __name__ == '__main__':
    with open('data/day01.txt', 'r') as f:
        instructions = f.read()

    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            raise Exception('Unexpected input')

    print(f'final floor is {floor}')
