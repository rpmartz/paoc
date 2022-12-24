import unittest

from python.aoc.y22.day19 import parse_blueprint


class Day19(unittest.TestCase):

    def test_parsing_first_line(self):
        text = 'Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 13 clay. Each geode robot costs 5 ore and 7 obsidian.'
        blueprint = parse_blueprint(text)

        self.assertEqual(1, blueprint.num)
        self.assertEqual(3, blueprint.ore_robot_cost)
        self.assertEqual(4, blueprint.clay_robot_cost)
        self.assertEqual(2, blueprint.obsidian_robot_ore_cost)
        self.assertEqual(13, blueprint.obsidian_robot_clay_cost)
        self.assertEqual(5, blueprint.geode_robot_ore_cost)
        self.assertEqual(7, blueprint.geode_robot_obsidian_cost)
