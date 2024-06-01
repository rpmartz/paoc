from collections import Counter

problem_start_template = 'OFSNKKHCBSNKBKFFCVNB'


def read_rules():
    with open('data/day14.txt', 'r') as f:
        return f.read()


def parse_rules(rules: str):
    pair_mappings = {}
    for pairing in rules.splitlines():
        lhs, rhs = pairing.split('->')
        pair_mappings[lhs.strip()] = rhs.strip()

    return pair_mappings


def process(pair_counts, rules: dict):
    updated_counts = Counter()
    for pair, count in pair_counts.items():
        new_char = rules[pair]

        # new pair one = first + new_char
        updated_counts[pair[0] + new_char] += count
        # new pair two = new_char + second
        updated_counts[new_char + pair[1]] += count

    return updated_counts


# this needs to take in a counter and then calculate frequencies
def quantify(pair_counts: Counter):
    digit_counts = Counter()

    for pair, count in pair_counts.items():
        digit_counts[pair[0]] += count
        digit_counts[pair[1]] += count

    # every letter is counted twice except for the first and the last, so add one to
    return (max(digit_counts.values()) - min(digit_counts.values())) // 2 + 1


def pairs(polymer_string: str) -> Counter:
    counter = Counter()
    for a, b in zip(polymer_string, polymer_string[1:]):
        counter[a + b] += 1

    return counter


if __name__ == '__main__':

    rules = parse_rules(read_rules())

    pair_counts = pairs(problem_start_template)
    for i in range(40):
        pair_counts = process(pair_counts, rules)
        if i == 9:
            print(f'Part 1: {quantify(pair_counts)}')

    print(f'Part 2: {quantify(pair_counts)}')
