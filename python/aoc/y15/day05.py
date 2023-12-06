with open('data/day05.txt') as f:
    lines = f.read().splitlines()

is_nice = lambda it: (any(it[i:i + 2] in it[:i] for i in range(len(it) - 1)) and
                      any(a == b for a, b in zip(it, it[2:])))

print(sum(map(is_nice, lines)))