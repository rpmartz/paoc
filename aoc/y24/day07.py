import re

def potential_values(i, nums, memo = {}):
    if i == 0:
        memo[0] = [nums[0]]

    else:
        # loop over all potential values available here
        potential_values = []
        for potential_value in memo[i - 1]:
            potential_values.append(nums[i] + potential_value)
            potential_values.append(nums[i] * potential_value)

        memo[i] = potential_values

    return memo

def is_valid(sum, nums):
    values_by_idx = {}
    for i, _ in enumerate(nums):
        values_by_idx = potential_values(i, nums, values_by_idx)

    possible_vals = set()

    # only valid if sum is at the end, i.e. possible by
    # using every character
    for n in values_by_idx[len(nums) - 1]:
        possible_vals.add(n)

    return sum in possible_vals

with open('data/day07.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

result = 0

for line in lines:
     all_nums = list(map(int, re.findall(r'\d+', line)))
     equation_sum = all_nums[0]
     nums = all_nums[1:]

     if is_valid(equation_sum, nums):
        result += equation_sum


print(result)