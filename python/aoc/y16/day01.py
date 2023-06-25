with open('data/day01.txt', 'r') as f:
    directions = f.read()

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

