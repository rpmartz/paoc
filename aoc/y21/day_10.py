def find_corruption(sequence):
    openers = {'{', '(', '[', '<'}
    closers = {'}', ')', ']', '>'}

    closers_to_openers = {
        '}': '{', ')': '(', '>': '<', ']': '['
    }

    stack = []
    for character in sequence:
        if character in openers:
            stack.append(character)
        elif character in closers:
            last_opener = stack.pop()
            expected_opener = closers_to_openers[character]
            if last_opener != expected_opener:
                return character

    return None


def find_completion(sequence):
    openers = {'{', '(', '[', '<'}
    closers = {'}', ')', ']', '>'}

    openers_to_closers = {
        '{': '}', '(': ')', '<': '>', '[': ']'
    }

    stack = []
    for character in sequence:
        if character in openers:
            stack.append(character)
        elif character in closers:
            stack.pop()

    needed_closers = []
    while stack:
        opener = stack.pop()
        needed_closers.append(openers_to_closers[opener])

    return ''.join(needed_closers)


def do_part_two(lines):
    scores = {
        ')': 1, ']': 2, '}': 3, '>': 4
    }

    all_scores = []

    for line in lines:
        if find_corruption(line):
            continue
        completion = find_completion(line)
        score = 0
        for closer in completion:
            score = (score * 5) + scores[closer]

        all_scores.append(score)

    print(sorted(all_scores)[len(all_scores) // 2])


def do_part_1(lines):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    score = 0
    for line in lines:
        first_illegal_character = find_corruption(line)
        if first_illegal_character:
            score += scores[first_illegal_character]

    print(score)


with open('data/day10.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

do_part_two(lines)
