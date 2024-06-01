with open('data/day08.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def find_unique_length_values(signals):
    one = None
    four = None
    seven = None
    eight = None

    for signal in signals:
        if len(signal) == 2:
            one = signal
        elif len(signal) == 3:
            seven = signal
        elif len(signal) == 4:
            four = signal
        elif len(signal) == 7:
            eight = signal

    return one, four, seven, eight


def do_part_one(lines):
    unique_segment_lengths = {2, 3, 4, 7}

    digit_count = 0

    for line in lines:
        output_values = line.split('|')[1]

        for code in output_values.split():
            if len(code) in unique_segment_lengths:
                digit_count += 1

    print(digit_count)


def do_part_two(lines):
    numbers = []
    for line in lines:
        lhs, rhs = line.split('|')
        both_parts = lhs.split() + rhs.split()

        one, four, seven, eight = find_unique_length_values(both_parts)

        four = set(four)
        seven = set(seven)

        number = ''
        for signal in rhs.split():
            length_of_signal = len(signal)
            if length_of_signal == 2:
                number += '1'
            elif length_of_signal == 3:
                number += '7'
            elif length_of_signal == 4:
                number += '4'
            elif length_of_signal == 5:
                len_xor_seven = len(seven ^ set(signal))
                len_xor_four = len(four ^ set(signal))
                if len_xor_four == 5 and len_xor_seven == 4:
                    number += '2'
                elif len_xor_four == 3 and len_xor_seven == 2:
                    number += '3'
                elif len_xor_four == 3 and len_xor_seven == 4:
                    number += '5'
                else:
                    raise Exception('Length 5 signal %s unmappable' % signal)
            elif length_of_signal == 6:
                len_xor_seven = len(seven ^ set(signal))
                len_xor_four = len(four ^ set(signal))
                if len_xor_four == 2 and len_xor_seven == 3:
                    number += '9'
                elif len_xor_four == 4 and len_xor_seven == 5:
                    number += '6'
                elif len_xor_four == 4 and len_xor_seven == 3:
                    number += '0'
                else:
                    raise Exception('Length 6 signal %s unmappable' % signal)
            elif length_of_signal == 7:
                number += '8'
            else:
                raise Exception('Signal %s unmappable' % signal)

        numbers.append((int(number)))

    print(sum(numbers))


do_part_one(lines)
do_part_two(lines)

# If you model each number as a 7 bit base 2 number where a is index 0 and f is index 7

# 0 - 1110111
# 1 - 0010010
# 2 - 1011101
# 3 - 1011010
# 4 - 0111010
# 5 - 1101010
# 6 - 1101111
# 7 - 1010010
# 8 - 1111111
# 9 - 1111011

# then you can look at the unique numbers:
# 1 - 0010010
# 4 - 0111010
# 7 - 1010010
# 8 - 1111111

# and given the example:
# 0 - 1110111 cagedb
# 1 - 0010010 ab
# 2 - 1011101 gcdfa
# 3 - 1011010 fbcad
# 4 - 0111010 eafb
# 5 - 1101010 cdfbe
# 6 - 1101111 cdfgeb
# 7 - 1010010 dab
# 8 - 1111111 acedgfb
# 9 - 1111011 cefabd

# we need a way to differentiate (acdfg, abcdf, bcdef) from one another
# and (abcdef, bcdefg, abcdeg) from one another using just ab, abfe, abd, and abcdefg and some setwise operator

five_letters = ['acdfg', 'fbcad', 'cdfbe']
six_letters = ['cefabd', 'cdfgeb', 'cagedb']

known_values = ['ab', 'abfe', 'abd', 'abcdefg']

for signal in six_letters:
    print('Signal %s' % signal)
    s = set(signal)
    for kv in known_values:
        kv_set = set(kv)
        print('\t ^ %s: %s' % (kv, len(s ^ kv_set)))

# for 5 signal values xor with 8 produces length 2 for all so it's not a differentiator
# for 5 signal values xor with 7 and 4 produces a combo of resulting set lengths (5, 4), (3, 2), and (3, 4)
# for 6 signal values xor with 7 and 4 produces a combo of resulting set lengths (2, 3), (4, 5), and (4, 3)
