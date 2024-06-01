from io import StringIO


class Packet:

    def __init__(self, version, type_id, literal_value=None, children=None):
        self.version = version
        self.type_id = type_id
        self.literal_value = literal_value
        self.children = children or []

    def version_sum(self):
        version_sum = self.version
        for child in self.children:
            version_sum += child.version_sum()

        return version_sum

    def calculate(self):
        subexpression_results = [child.calculate() for child in self.children]
        if self.type_id == 0:
            return sum(subexpression_results)
        elif self.type_id == 1:
            accum = 1
            for val in subexpression_results:
                accum = accum * val

            return accum
        elif self.type_id == 2:
            return min(subexpression_results)
        elif self.type_id == 3:
            return max(subexpression_results)
        elif self.type_id == 4:
            return self.literal_value
        elif self.type_id == 5:
            if subexpression_results[0] > subexpression_results[1]:
                return 1

            return 0
        elif self.type_id == 6:
            if subexpression_results[0] < subexpression_results[1]:
                return 1

            return 0
        elif self.type_id == 7:
            if subexpression_results[0] == subexpression_results[1]:
                return 1

            return 0

    def __eq__(self, other):
        return isinstance(other,
                          Packet) and self.version == other.version and self.type_id == other.type_id and self.children == other.children


def hex_to_bin(hex_string):
    hex_to_bin = {"0": "0000",
                  "1": "0001",
                  "2": "0010",
                  "3": "0011",
                  "4": "0100",
                  "5": "0101",
                  "6": "0110",
                  "7": "0111",
                  "8": "1000",
                  "9": "1001",
                  "A": "1010",
                  "B": "1011",
                  "C": "1100",
                  "D": "1101",
                  "E": "1110",
                  "F": "1111"}
    bits = []
    for hex_val in hex_string:
        bits.append(hex_to_bin[hex_val])

    return ''.join(bits)


def parse_literal(binary_str: StringIO) -> int:
    literal = 0
    while True:
        first_bit = int(binary_str.read(1), 2)
        # shifting left and then ORing with the next 4 bits is like appending
        # the string values to the end of a string
        literal = (literal << 4) | int(binary_str.read(4), 2)

        if first_bit == 0:
            break

    return literal


def parse_packets(binary_str: StringIO):
    packets = []
    while True:
        try:
            packets.append(parse_packet(binary_str))
        except Exception:
            return packets


def parse_packet(binary_str: StringIO) -> Packet:
    version = int(binary_str.read(3), 2)
    type_id = int(binary_str.read(3), 2)

    if type_id == 4:
        literal_value = parse_literal(binary_str)
        return Packet(version, type_id, literal_value)
    else:
        length_type_id = int(binary_str.read(1))
        if length_type_id == 0:
            # next 15 bits are a number that represents the total length in bits of the sub-packets contained in the packet
            num_bits = int(binary_str.read(15), 2)
            children = parse_packets(StringIO(binary_str.read(num_bits)))
        elif length_type_id == 1:
            # next 11 bits are number that represents number of sub-packets contained in the packet
            num_sub_packets = int(binary_str.read(11), 2)
            children = [parse_packet(binary_str) for _ in range(num_sub_packets)]

        return Packet(version, type_id, children=children)


if __name__ == '__main__':
    with open('data/day16.txt', 'r') as f:
        hex = f.read()

    packet = parse_packet(StringIO(hex_to_bin(hex.strip())))
    print(packet.version_sum())
    print(packet.calculate())
