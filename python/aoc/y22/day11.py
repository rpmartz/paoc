from dataclasses import dataclass


@dataclass
class Monkey:
    items: [int]
    truthy_dest: int
    falsey_dest: int
    num_inspected: int


def operation(monkey_num, item):
    intermediate_result = 0
    if monkey_num == 0:
        intermediate_result = item * 2
    elif monkey_num == 1:
        intermediate_result = item * 13
    elif monkey_num == 2:
        intermediate_result = item + 5
    elif monkey_num == 3:
        intermediate_result = item + 6
    elif monkey_num == 4:
        intermediate_result = item + 1
    elif monkey_num == 5:
        intermediate_result = item + 4
    elif monkey_num == 6:
        intermediate_result = item + 2
    elif monkey_num == 7:
        intermediate_result = item * item

    return intermediate_result % (5 * 2 * 19 * 7 * 17 * 13 * 3 * 11)


def test_item(monkey_num, item):
    if monkey_num == 0:
        return item % 5 == 0
    elif monkey_num == 1:
        return item % 2 == 0
    elif monkey_num == 2:
        return item % 19 == 0
    elif monkey_num == 3:
        return item % 7 == 0
    elif monkey_num == 4:
        return item % 17 == 0
    elif monkey_num == 5:
        return item % 13 == 0
    elif monkey_num == 6:
        return item % 3 == 0
    elif monkey_num == 7:
        return item % 11 == 0

monkeys = [
    Monkey([98, 89, 52], 6, 1, 0),  # 0
    Monkey([57, 95, 80, 92, 57, 78], 2, 6, 0),  # 1
    Monkey([82, 74, 97, 75, 51, 92, 83], 7, 5, 0),  # 2
    Monkey([97, 88, 51, 68, 76], 0, 4, 0),  # 3
    Monkey([63], 0, 1, 0),  # 4
    Monkey([94, 91, 51, 63], 4, 3, 0),  # 5
    Monkey([61, 54, 94, 71, 74, 68, 98, 83], 2, 7, 0),  # 6
    Monkey([90, 56], 3, 5, 0)  # 7
]


def run(num_rounds):
    for _ in range(num_rounds):
        for i, m in enumerate(monkeys):
            for item in m.items:
                newval = operation(i, item)
                if test_item(i, newval):
                    monkeys[m.truthy_dest].items.append(newval)
                else:
                    monkeys[m.falsey_dest].items.append(newval)

                m.num_inspected += 1

            m.items = []

    inspection_counts = [m.num_inspected for m in monkeys]
    inspection_counts.sort()
    print(f'counts: {inspection_counts}')
    print(f'answer: {inspection_counts[-1] * inspection_counts[-2]}')


run(10000)
