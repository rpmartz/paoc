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
    has_two_pairs = any([a in pw and b in pw for a, b in product(letter_pairs,  repeat=2)])

    return all([has_ascending_run, no_banned_chars, has_two_pairs])

def increment_password(pw):
    orig = pw
    index = len(pw) - 1
    while index > -1:
        if pw != orig and meets_requirement(pw):
            return pw
        elif pw[index] == 'z':
            index -= 1
        else:
            char_at_index = pw[index]

            i = digits_to_index[char_at_index]

            new_char = index_to_digits[(i + 1) % 25]
            print(f'current char {char_at_index} with index {i} updated to {new_char}')

            pw_chars = list(pw)
            pw_chars[index] = new_char
            pw = ''.join(pw_chars)
            print(f'new password: {pw}')




if __name__ == "__main__":
    next_password = increment_password('abcdefgh')
    print(f'next password: {next_password}')
