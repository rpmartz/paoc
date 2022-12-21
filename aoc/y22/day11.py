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

    return intermediate_result // 3


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
