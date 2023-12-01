import re
def lookup_digit(d: str):
    word_to_digit = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }

    if d.isnumeric():
        return d

    return word_to_digit[d]


if __name__ == "__main__":
    with open("data/day01.txt", "r") as ifile:
        lines = [l.strip() for l in ifile.readlines()]

    nums = []
    for line in lines:
        nums_in_line = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        if nums_in_line:
            first = lookup_digit(nums_in_line[0])
            second = lookup_digit(nums_in_line[-1])
            nums.append(int("".join([first, second])))


    print(sum(nums))
