with open('data/day01.txt', 'r') as f:
    directions = [d.strip() for d in f.read().split(',')]

cardinal_directions = {'N', 'S', 'E', 'W'}
turn_directions = {'L', 'R'}

def new_heading(current_heading, instruction_direction):
    assert current_heading in cardinal_directions
    assert instruction_direction in turn_directions

    heading_map = {
        'N': {'R': 'E', 'L': 'W'},
        'S': {'R': 'W', 'L': 'E'},
        'E': {'R': 'S', 'L': 'N'},
        'W': {'R': 'N', 'L': 'S'}
    }

    return heading_map[current_heading][instruction_direction]

def parse_dir(direction):
    turn_dir = direction[0]
    magnitude = int(direction[1:])

    return turn_dir, magnitude

current_heading = 'N'
location = (0, 0)

for direction in directions:
    turn_dir, distance = parse_dir(direction)
    current_heading = new_heading(current_heading, turn_dir)
    if current_heading == 'N':
        location = (location[0], location[1] + distance)
    elif current_heading == 'S':
        location = (location[0], location[1] - distance)
    elif current_heading == 'E':
        location = (location[0] + distance, location[1])
    elif current_heading == 'W':
        location = (location[0] - distance, location[1])

print(f'Location is {location}')
print(f'Manhattan distance is {abs(location[0] - 0) + abs(location[1] - 0)}')