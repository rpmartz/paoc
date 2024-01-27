from python.aoc.common.text import alphabet
from itertools import product

password = "hepxcrrq"

abet = alphabet()

triplets = [abet[i : i + 3] for i in range(len(abet) - 4)]
banned_chars = ["i", "o", "l"]
letter_pairs = [l * 2 for l in abet]


def meets_requirement(pw) -> bool:
    has_ascending_run = any([triplet in pw for triplet in triplets])
    no_banned_chars = all([c not in pw for c in banned_chars])
    has_two_pairs = any([a in pw and b in pw for a, b in product(letter_pairs,  repeat=2)])

    return all([has_ascending_run, no_banned_chars, has_two_pairs])


if __name__ == "__main__":
    for pw in ["hijklmmn", "abcdffaa", "ghjaabcc"]:
        print(f"{pw}: {meets_requirement(pw)}")