def build_target_grid(x_open, x_close, y_open, y_close):
    grid = set()
    for x in range(x_open, x_close + 1):
        for y in range(y_open, y_close - 1, -1):
            grid.add((x, y))

    return grid


def process_step(x, y):
    if x == 0:
        d_x = 0
    elif x > 0:
        d_x = -1
    else:
        d_x = 1

    new_x = x + d_x
    new_y = y - 1
    return (new_x, new_y)


def find_max_height_for_initial_velocity(dx, dy, grid_x0, grid_x1, grid_y0, grid_y1):
    position = 0, 0
    max_height = 0
    while True:
        # update position based on vector
        position = position[0] + dx, position[1] + dy
        x, y = position
        max_height = max(max_height, y)

        # update velocity based on steps

        dx, dy = process_step(dx, dy)

        # check whether we have hit target and add max and exit if so
        within_x_bounds = grid_x0 <= x <= grid_x1
        within_y_bounds = grid_y0 <= y <= grid_y1
        if within_x_bounds and within_y_bounds:
            return max_height

        # check whether we are outside bounds of grid and exit if so
        missed_horizontally = (dx == 0 and x < grid_x0) or x > grid_x1
        missed_vertically = y < grid_y1
        if missed_horizontally or missed_vertically:
            return None

        # update velocity based on steps

        dx, dy = process_step(dx, dy)


if __name__ == '__main__':
    x0, x1, y0, y1 = 150, 171, -129, -70

    max_height = 0
    counts = 0
    for x_vel in range(1, 172):
        for y_vel in range(-129, 130):
            local_max = find_max_height_for_initial_velocity(x_vel, y_vel, x0, x1, y0, y1)
            if local_max:
                counts += 1
                max_height = max(max_height, local_max)
                print(f'({x_vel}, {y_vel}) with max height {local_max}')

    print(max_height)
    print(counts)
