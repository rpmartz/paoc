import math

def read_input():
    with open('data/day18.txt', 'r') as f:
        lines = f.readlines()
        return [eval(line.strip()) for line in lines]

def add(left, right):
    return [left, right]


def reduce(num):
    # if any pair is nested inside four pairs, the leftmost such pair explodes.

    # If any regular number is 10 or greater, the leftmost such regular number splits.

    pass


def explode(pair):
    assert len(pair == 2), f'len({pair}) = {len(pair)}. Expected 2'
    left = pair[0]
    right = pair[1]
    # add pair's left value to first regular number to left of exploding pair
    # add pair's right value to first regular number to right of exploding pair
    #

    pass

def split(i):
    return [math.floor(i / 2), math.ceil(i / 2)]

def magnitude(snailfish_num):
    if isinstance(snailfish_num, int):
        return snailfish_num
    return 3 * magnitude(snailfish_num[0]) + 2 * magnitude(snailfish_num[1])

if __name__ == '__main__':
    snailfish_num_list = read_input()
    reduce(eval('[[[[[9,8],1],2],3],4]'))
