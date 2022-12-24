from collections import namedtuple

HouseCoordinate = namedtuple('HouseCoordinate', ['x', 'y'])


def move(position: HouseCoordinate, movement: str) -> HouseCoordinate:
    if movement == '>':
        new_position = HouseCoordinate(position.x + 1, position.y)
    elif movement == '^':
        new_position = HouseCoordinate(position.x, position.y + 1)
    elif movement == '<':
        new_position = HouseCoordinate(position.x - 1, position.y)
    elif movement == 'v':
        new_position = HouseCoordinate(position.x, position.y - 1)
    else:
        raise RuntimeError(f'Unexpected instruction {movement}')

    return new_position


if __name__ == '__main__':
    with open('data/day03.txt', 'r') as infile:
        chars = infile.read()

    visited: set[HouseCoordinate] = set()

    santa_position = HouseCoordinate(0, 0)
    robot_santa_position = HouseCoordinate(0, 0)
    visited.add(santa_position)

    for index, instruction in enumerate(chars):
        if index % 2 == 0:
            santa_position = move(santa_position, instruction)
            visited.add(santa_position)
        else:
            robot_santa_position = move(robot_santa_position, instruction)
            visited.add(robot_santa_position)

    print(len(visited))
