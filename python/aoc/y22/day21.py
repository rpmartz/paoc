import ast

import operator


def read_lines():
    with open("data/day21.txt", "r") as ifile:
        return [l.strip() for l in ifile.readlines()]


operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def yell(monkey_name, job_table):
    job = job_table[monkey_name]

    if isinstance(job, int):
        return job
    else:
        lhs, op, rhs = job.split(" ")

        operation = operators[op]
        return operation(yell(lhs, job_table), yell(rhs, job_table))


if __name__ == "__main__":
    lines = read_lines()

    lookup_table = {}
    constants = set()
    for line in lines:
        components = line.split(":")
        lhs = components[0]
        rhs = components[1].strip()

        if rhs.isnumeric():
            lookup_table[lhs] = int(rhs)
            constants.add(lhs)
        else:
            lookup_table[lhs] = rhs

    print(yell("root", lookup_table))
