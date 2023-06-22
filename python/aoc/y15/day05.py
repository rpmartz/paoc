import os

with open('data/day05.txt') as f:
    lines = f.read().splitlines()

is_nice = lambda s: any(a == b for a, b in zip(s, s[2:]))

def has_repeating_pair(line):
    for i in range(len(line) - 1):
        if line[i:i+2] in line[:i]:
            return True

def has_valid_triple(line):
    for a, b in zip(line, line[2:]):
        if a == b:
            return True


count = 0

for line in lines:
    has_pair = False
    valid_triple = False

    if has_repeating_pair(line):
        has_pair = True
    if has_valid_triple(line):
        valid_triple = True

    if has_pair and valid_triple:
        count += 1

# print(sum(map(is_nice, lines)))
print(count)