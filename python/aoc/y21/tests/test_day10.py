import unittest

from day_10 import *


class DayTenTests(unittest.TestCase):

    def test_corrupted_samples(self):
        line = '{([(<{}[<>[]}>{[]{[(<()>'
        c = find_corruption(line)
        self.assertEqual(c, '}')

        line = '[[<[([]))<([[{}[[()]]]'
        c = find_corruption(line)
        self.assertEqual(c, ')')

        line = '[{[{({}]{}}([{[{{{}}([]'
        c = find_corruption(line)
        self.assertEqual(c, ']')

        line = '[<(<(<(<{}))><([]([]()'
        c = find_corruption(line)
        self.assertEqual(c, ')')

        line = '<{([([[(<>()){}]>(<<{{'
        c = find_corruption(line)
        self.assertEqual(c, '>')

    def test_find_completion(self):
        line = '[({(<(())[]>[[{[]{<()<>>'
        completion = find_completion(line)
        self.assertEqual(completion, '}}]])})]')
