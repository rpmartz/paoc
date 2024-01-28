from python.aoc.common.text import alphabet
from itertools import product

password = "hepxcrrq"

abet = alphabet()

triplets = [abet[i : i + 3] for i in range(len(abet) - 4)]
banned_chars = ["i", "o", "l"]
letter_pairs = [l * 2 for l in abet]

digits_to_index = dict(zip(abet, range(len(abet))))
index_to_digits = dict(zip(range(len(abet)), abet))


def meets_requirement(pw) -> bool:
    has_ascending_run = any([triplet in pw for triplet in triplets])
    no_banned_chars = all([c not in pw for c in banned_chars])
    has_two_pairs = any(
        [a != b and a in pw and b in pw for a, b in product(letter_pairs, repeat=2)]
    )

    return all([has_ascending_run, no_banned_chars, has_two_pairs])


def increment_password(pw):
    orig = pw
    index = len(pw) - 1
    while index > -1:
        if pw != orig and meets_requirement(pw):
            return pw

        # bcz -> bda, bdb, bdc ...
        # bzz -> caa
        else:
            pw_chars = list(pw)
            char_at_index = pw[index]
            if char_at_index == "z":
                print(
                    f"char at idx {index} in pw {pw} is z, setting to a and moving back"
                )
                pw_chars[index] = "a"
                index -= 1
            else:
                curr_dig_i = digits_to_index[char_at_index]
                next_char = index_to_digits[curr_dig_i + 1]

                pw_chars[index] = next_char

        pw = "".join(pw_chars)
        index -= 1


if __name__ == "__main__":
    next_password = increment_password("abcdefgh")
    print(f"next password: {next_password}")
