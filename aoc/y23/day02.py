

with open('data/day02.txt', 'r') as ifile:
    lines = [l.strip() for l in ifile.readlines()]


games = {}

for line in lines:
    components = line.split(':')
    game_no = components[0].split(' ')[-1]

    roll_data = components[1]

    handfulls = roll_data.split(';')

    reds = []
    blues = []
    greens = []

    for handfull in handfulls:
        combos = handfull.split(',')

        for quantity in combos:
            q_stripped = quantity.strip()
            if 'red' in q_stripped:
                reds.append(int(q_stripped.replace(' red', '')))
            elif 'blue' in q_stripped:
                blues.append(int(q_stripped.replace(' blue', '')))
            elif 'green' in q_stripped:
                greens.append(int(q_stripped.replace(' green', '')))
            else:
                raise ValueError(f'Unexpected value {quantity}')

    games[int(game_no)] = {
        'red': max(reds),
        'blue': max(blues),
        'green': max(greens)
    }

total = 0
for game, mins in games.items():
    reds = max(mins['red'], 1)
    blues = max(mins['blue'], 1)
    greens = max(mins['green'], 1)

    power = reds * blues * greens
    total += power

print(total)
