import unittest

from python.aoc.y15.day11 import meets_requirement, increment_password

class Y15Day11Test(unittest.TestCase):

    def test_example_passwords(self):
        self.assertFalse(meets_requirement('hijklmmn'))
        self.assertFalse(meets_requirement('abbceffg'))
        self.assertFalse(meets_requirement('abbcegjk'))
        self.assertFalse(meets_requirement('abbcegjk'))
        self.assertTrue(meets_requirement('abcdffaa'))
        self.assertTrue(meets_requirement('ghjaabcc'))

    def test_increment_password(self):
        self.assertEqual('abcdffaa', increment_password('abcdefgh'))
        self.assertEqual('abcdffaa', increment_password('ghijklmn'))

