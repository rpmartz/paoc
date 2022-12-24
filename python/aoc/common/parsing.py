import re


def ints(s):
    """Finds all the integers in a string"""
    return [int(v) for v in re.findall("-?[0-9]+", s)]
