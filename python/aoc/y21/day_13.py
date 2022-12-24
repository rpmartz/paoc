def read_points():
    with open('data/day13-points.txt', 'r') as f:
        return [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in f.readlines()]


def read_folds():
    with open('data/day13-folds.txt', 'r') as f:
        return [(line.split('=')[0], int(line.split('=')[1])) for line in f.readlines()]


def process_fold(points, fold):
    axis, value = fold
    if axis == 'x':
        return {(x, y) if x <= value else (2 * value - x, y)
                for (x, y) in points}
    else:
        return {(x, y) if y <= value else (x, 2 * value - y)
                for (x, y) in points}


if __name__ == '__main__':
    points = read_points()
    folds = read_folds()

    for fold in folds:
        points = process_fold(points, fold)

    lines = []

    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in points:
                print('o', end='')
            else:
                print(' ', end='')

        print('')
