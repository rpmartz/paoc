from itertools import cycle

if __name__ == '__main__':

    die = cycle(range(1, 101))
    scores = [0, 0]
    positions = [2, 8]
    turn = 1
    num_rolls = 0

    while True:
        steps = next(die) + next(die) + next(die)
        num_rolls += 3

        if turn == 1:
            positions[0] = ((positions[0] + steps - 1) % 10) + 1
            scores[0] += positions[0]
            turn = 2
        elif turn == 2:
            positions[1] = ((positions[1] + steps - 1) % 10) + 1
            scores[1] += positions[1]
            turn = 1

        if scores[0] >= 1000 or scores[1] >= 1000:
            min_score = min(scores)
            print(f'Losing score: {min_score}. Num rolls: {num_rolls}. Product = {num_rolls * min_score}')
            break
