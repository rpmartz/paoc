import unittest

from day_16 import *


class DaySixteen(unittest.TestCase):

    def test_D2FE28(self):
        hex = 'D2FE28'
        expected = '110100101111111000101000'
        actual = hex_to_bin(hex)
        self.assertEqual(expected, actual)

    def test_38006F45291200(self):
        hex = '38006F45291200'
        expected = '00111000000000000110111101000101001010010001001000000000'
        actual = hex_to_bin(hex)
        self.assertEqual(expected, actual)

    def test_example_literal(self):
        hex = 'D2FE28'

        expected = Packet(version=6, type_id=4, literal_value=2021)
        actual = parse_packet(StringIO(hex_to_bin(hex)))

        self.assertEqual(expected, actual)

    def test_first_example_operator_packet(self):
        hex = '38006F45291200'

        expected = Packet(version=1, type_id=6, children=[
            Packet(version=6, type_id=4, literal_value=10),
            Packet(version=2, type_id=4, literal_value=20)
        ])
        actual = parse_packet(StringIO(hex_to_bin(hex)))

        self.assertEqual(expected, actual)

    def test_second_example_operator_packet(self):
        hex = 'EE00D40C823060'

        expected = Packet(version=7, type_id=3, children=[
            Packet(version=2, type_id=4, literal_value=1),
            Packet(version=4, type_id=4, literal_value=2),
            Packet(version=1, type_id=4, literal_value=3)
        ])
        actual = parse_packet(StringIO(hex_to_bin(hex)))

        self.assertEqual(expected, actual)

    def test_version_sum_first_example(self):
        hex = '8A004A801A8002F478'
        packet = parse_packet(StringIO(hex_to_bin(hex)))

        self.assertEqual(16, packet.version_sum())

    def test_version_sum_last_example(self):
        hex = 'A0016C880162017C3686B18A3D4780'
        packet = parse_packet(StringIO(hex_to_bin(hex)))

        self.assertEqual(31, packet.version_sum())
