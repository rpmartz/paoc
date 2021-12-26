if __name__ == '__main__':
    with open('data/day01.txt', 'r') as f:
        instructions = f.read()

    floor = 0
    entered_basement = False
    for index, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1

        if not entered_basement and floor < 0:
            entered_basement = True
            # instruction number is index + 1 since index starts at 0
            print(f'Entered basement at instruction number {index + 1}')

    print(f'final floor is {floor}')
