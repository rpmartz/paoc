import time
from functools import lru_cache


def read_file():
    with open('data/day07.txt', 'r') as f:
        return [int(num) for num in f.read().split(',')]


# program performance ends up being heavily dependent upon having a cache
# of sufficient size that you minimize recalculation
@lru_cache(maxsize=2000)
def total_cost(num_steps):
    cost = 0
    cost_per_step = 1
    for i in range(0, num_steps):
        cost = cost + cost_per_step
        cost_per_step += 1

    return cost


def find_best_alignment(positions, cost_fn):
    min_distance = 999999999999999
    best_position = None
    for number in positions:
        distance_for_number = sum(cost_fn(abs(number - point)) for point in positions)

        if distance_for_number < min_distance:
            min_distance = distance_for_number
            best_position = number

    return best_position, min_distance


if __name__ == '__main__':
    starting_positions = read_file()
    best_position, fuel_cost = find_best_alignment(starting_positions, lambda x: x)
    print(fuel_cost)

    start = time.perf_counter()
    _, fuel_cost = find_best_alignment(starting_positions, total_cost)
    end = time.perf_counter()

    print('Average execution time over 3 runs without memoization: 34.4s (previously calculated)')
    print('Execution time with memoization: %s' % "{:.2f}".format(end - start))

    print(total_cost.cache_info())
    print(fuel_cost)
