import os

def read_input():
    with open('data/day18.txt', 'r') as f:
        lines = f.readlines()
        return [eval(line.strip()) for line in lines]

def add(left, right):
    # form a pair from the left and right snailfish parameters
    pass


def reduce():
    # if any pair is nested inside 4 pairs, leftmost pair explodes
    # if any regular number is 10 or greater, leftmost regular pair splits
    # do this until done (recursion?)
    pass


def explode():
    # add pair's left value to first regular number to left of exploding pair
    # add pair's right value to first regular number to right of exploding pair
    #
    pass


if __name__ == '__main__':
    print(read_input())
