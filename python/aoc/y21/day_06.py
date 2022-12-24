from collections import Counter


def process_day(fish_list):
    new_fish = []
    for index, days_left in enumerate(fish_list):
        if days_left == 0:
            new_fish.append(8)
            fish_list[index] = 6
        else:
            fish_list[index] = fish_list[index] - 1

    if new_fish:
        fish_list.extend(new_fish)


if __name__ == '__main__':
    with open('data/day06.txt', 'r') as f:
        starting_state = f.read()
        fish_counts = Counter([int(val) for val in starting_state.split(',')])

    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        fish[i] = fish_counts[i]

    for day in range(0, 256):

        # zeros will hatch today
        new_fish = fish[0]
        for i in range(1, len(fish)):
            # everything else becomes one day closer to hatching
            fish[i - 1] = fish[i]

        # just hatched fish are "eights"
        fish[8] = new_fish

        # fish that just had babies are "sevens" again
        fish[6] = fish[6] + new_fish

    print(sum(fish))
