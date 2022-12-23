def compare_packet(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, int):
        return compare_packet(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare_packet([left], right)
    else:
        for left_el, right_el in zip(left, right):
            if left_el != right_el:
                return compare_packet(left_el, right_el)

        return compare_packet(len(left), len(right))
