import re
from collections import namedtuple

blueprint_regex = 'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'

Blueprint = namedtuple('Blueprint',
                       'num, ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost')


def get_input():
    with open('data/day19.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def parse_blueprint(line):
    [(num, ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost,
      geode_robot_obsidian_cost)] = re.findall(blueprint_regex, line)

    return Blueprint(int(num), int(ore_robot_cost), int(clay_robot_cost), int(obsidian_robot_ore_cost),
                     int(obsidian_robot_clay_cost), int(geode_robot_ore_cost), int(geode_robot_obsidian_cost))


bp = parse_blueprint(sample_input)
print(bp)
