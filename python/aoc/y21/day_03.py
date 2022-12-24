def read_file():
    with open('data/day03.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def build_index_to_bit_count_map(lines):
    positions_to_bit_counts = {
        0: {'0': 0, '1': 0},
        1: {'0': 0, '1': 0},
        2: {'0': 0, '1': 0},
        3: {'0': 0, '1': 0},
        4: {'0': 0, '1': 0},
        5: {'0': 0, '1': 0},
        6: {'0': 0, '1': 0},
        7: {'0': 0, '1': 0},
        8: {'0': 0, '1': 0},
        9: {'0': 0, '1': 0},
        10: {'0': 0, '1': 0},
        11: {'0': 0, '1': 0}
    }

    for line in lines:
        for index, bit in enumerate(line):
            bit_count_for_index = positions_to_bit_counts[index]

            count_for_bit_at_index = bit_count_for_index[bit]
            count_for_bit_at_index += 1
            bit_count_for_index[bit] = count_for_bit_at_index

            positions_to_bit_counts[index] = bit_count_for_index

    return positions_to_bit_counts


def part_one(lines):
    positions_to_bit_counts = build_index_to_bit_count_map(lines)

    result = []
    for bit_count in positions_to_bit_counts.values():
        if bit_count['0'] > bit_count['1']:
            result.append('0')
        else:
            result.append('1')

    gamma = int(''.join(result), 2)
    inverse = int('111111111111', 2)
    epsilon = gamma ^ inverse

    print('gamma: %d' % (gamma))
    print('epsilon: %d' % (epsilon))
    print('gamma * epsilon = %d' % (gamma * epsilon))


def take_where(binary_strings, position, value):
    """
    Filters a collection of binary strings whose value at index `position` are equal to `value`
    """

    # defensive checks
    assert position < 12
    assert value in {'0', '1'}

    result = []
    for binary_string in binary_strings:
        if binary_string[position] == value:
            result.append(binary_string)

    return result


def find_o2_gen_rating(lines, ):
    o2_gen_rating = None
    o2_results = lines
    for i in range(0, 12):
        positions_to_bit_counts = build_index_to_bit_count_map(o2_results)
        bit_counts = positions_to_bit_counts[i]
        if bit_counts['0'] == bit_counts['1']:
            more_freq_bit = '1'
        elif bit_counts['0'] > bit_counts['1']:
            more_freq_bit = '0'
        else:
            more_freq_bit = '1'

        o2_results = take_where(o2_results, i, more_freq_bit)
        if len(o2_results) == 1:
            o2_gen_rating = o2_results[0]
            break

    if o2_gen_rating is None:
        raise Exception('Could not find O2 rating')

    o2_gen_as_int = int(''.join(o2_gen_rating), 2)
    print('o2 gen rating of [%s] is %d' % (o2_gen_rating, o2_gen_as_int))

    return o2_gen_as_int


def find_co2_scrubber_rating(lines):
    co2_scrubber_rating = None
    co2_results = lines
    for i in range(0, 12):
        positions_to_bit_counts = build_index_to_bit_count_map(co2_results)
        bit_counts = positions_to_bit_counts[i]
        if bit_counts['0'] == bit_counts['1']:
            less_frequent_bit = '0'
        elif bit_counts['0'] < bit_counts['1']:
            less_frequent_bit = '0'
        else:
            less_frequent_bit = '1'

        co2_results = take_where(co2_results, i, less_frequent_bit)
        if len(co2_results) == 1:
            co2_scrubber_rating = co2_results[0]
            break

    if co2_scrubber_rating is None:
        raise Exception('Could not find CO2 scrubber rating')

    co2_scrubber_rtg_as_int = int(''.join(co2_scrubber_rating), 2)
    print('o2 gen rating of [%s] is %d' % (co2_scrubber_rating, co2_scrubber_rtg_as_int))

    return co2_scrubber_rtg_as_int


def part_two(lines):
    co2_scrubber_as_int = find_co2_scrubber_rating(lines)
    o2_gen_rating_as_int = find_o2_gen_rating(lines)

    print(co2_scrubber_as_int * o2_gen_rating_as_int)


if __name__ == '__main__':
    lines = read_file()
    part_one(lines)

    print('\n=== part two ===\n')
    part_two(lines)
