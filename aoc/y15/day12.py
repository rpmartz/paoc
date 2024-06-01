import json
def read_input():
    with open('data/day12.json', 'r') as f:
        return json.load(f)

def compute_sum(values, running_sum):
    pass


if __name__ == '__main__':
    parsed_json = read_input()

    for k, v in parsed_json.items():
        print(f'{k}: {v}')