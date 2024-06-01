def count_num_flashes(board):
    total_flashes = 0

    coord_grid = {}
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            coord_grid[(i, j)] = value

    num_steps = 0
    while True:
        num_steps += 1
        flashes_for_step = []

        for point, value in coord_grid.items():
            coord_grid[point] += 1
            if coord_grid[point] > 9:
                flashes_for_step.append(point)

        while flashes_for_step:
            point = flashes_for_step.pop()
            if coord_grid[point] == 0:
                continue

            coord_grid[point] = 0
            total_flashes += 1

            # also increment neighbors
            for neighbor in get_neighbors(point[0], point[1]):

                # ignore points of fboard
                if neighbor in coord_grid and coord_grid[neighbor] != 0:
                    coord_grid[neighbor] += 1

                    if coord_grid[neighbor] > 9:
                        flashes_for_step.append(neighbor)

        if all(value == 0 for value in coord_grid.values()):
            break

    return num_steps


def get_neighbors(i, j):
    neighbors = set()

    for x_offset in (-1, 0, 1):
        for y_offset in (-1, 0, 1):
            if x_offset == 0 and y_offset == 0:
                continue
            neighbors.add((i + x_offset, j + y_offset))

    return neighbors


def get_board():
    with open('data/day11.txt', 'r') as file:
        board = []
        for line in file.readlines():
            row = []
            for char in line.strip():
                row.append(int(char))
            board.append(row)

        return board


if __name__ == '__main__':
    board = get_board()
    print(count_num_flashes(board))
