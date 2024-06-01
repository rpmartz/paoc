import re
from typing import List


def ints(s):
    """Finds all the integers in a string"""
    return [int(v) for v in re.findall("-?[0-9]+", s)]

def split_and_parse(s: str, delimiter=",", parse_fn=int):
    xs = s.split(delimiter)
    return [parse_fn(x) for x in xs]
