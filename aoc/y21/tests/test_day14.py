import unittest

rules = parse_rules("""\
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""")


class DayFourteenTests(unittest.TestCase):

    def test_polymer_after_step_one(self):
        template = 'NNCB'
        expected = 'NCNBCHB'
        actual = process(template, rules)

        self.assertEqual(expected, actual)

    def test_polymer_after_step_two(self):
        template = 'NCNBCHB'
        expected = 'NBCCNBBBCBHCB'
        actual = process(template, rules)

        self.assertEqual(expected, actual)

    def test_polymer_after_step_three(self):
        template = 'NBCCNBBBCBHCB'
        expected = 'NBBBCNCCNBBNBNBBCHBHHBCHB'
        actual = process(template, rules)

        self.assertEqual(expected, actual)

    def test_polymer_after_step_four(self):
        template = 'NBBBCNCCNBBNBNBBCHBHHBCHB'
        expected = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
        actual = process(template, rules)

        self.assertEqual(expected, actual)

    def test_quantify(self):
        polymer = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
        expected = 18
        actual = quantify(polymer)

        self.assertEqual(expected, actual)
