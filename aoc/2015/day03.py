from collections import namedtuple

HouseCoordinate = namedtuple('HouseCoordinate', ['x', 'y'])


if __name__ == '__main__':
    with open('data/day03.txt', 'r') as infile:
        chars = infile.read()

    visited: set[HouseCoordinate] = set()

    current = HouseCoordinate(0, 0)
    visited.add(current)

    for instruction in chars:
        if instruction == '>':
            current = HouseCoordinate(current.x + 1, current.y)
        elif instruction == '^':
            current = HouseCoordinate(current.x, current.y + 1)
        elif instruction == '<':
            current = HouseCoordinate(current.x - 1, current.y)
        elif instruction == 'v':
            current = HouseCoordinate(current.x, current.y - 1)
        else:
            raise RuntimeError(f'Unexpected instruction {instruction}')

        visited.add(current)

    print(len(visited))




