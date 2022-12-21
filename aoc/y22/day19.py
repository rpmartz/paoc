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


def run(blueprints, num_minutes):
    for bp in blueprints:
        for m in range(num_minutes):
            print(f'executing min {m} for {bp.num}')


def part_one():
    num_minutes = 24
    lines = get_input()
    blueprints = [parse_blueprint(line) for line in lines]
    run(blueprints, num_minutes)


part_one()

# approach: greedy, dynamic programming, or backtracking/search?
# optimizing for num geodes
