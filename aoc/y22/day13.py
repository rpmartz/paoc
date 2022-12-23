def compare_packet(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
