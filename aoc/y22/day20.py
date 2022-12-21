def get_parsed_input():
    with open('data/day20.txt', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


# step 1 - find abs value of the delta and decrement it by len(list) until it's <= len(list)
# then check to make sure you don't need to make it negative


# case 1 positive and (value + idx) is less than (len(list) - idx) - straight move right
# case 2 positive and (value + idx) is greater than (len(list) - idx) - need to wrap around to front of list
# case 3 negative and (idx - abs(value)) is greater than 0 - straight move left
# case 4 negative and (idx - abs(value)) is less than 0 - need to wrap around to back of list

# def mix(original_idx, num, new_list, old_list):
#     n = len(old_list)
#     wrapped_index = num
#     while abs(wrapped_index) > n:
#         wrapped_index = wrapped_index - n # find wrapped position
#
#     new_list[wrapped_index] =

# nums = get_parsed_input()

nums = [1, 2, -3, 3, -2, 0, 4]

list_length = len(nums)
new_list = nums.copy()

for idx, num in enumerate(nums):
    # step 1 - find abs value of the delta and decrement it by len(list) until it's <= len(list)
    delta = num
    if num >= 0:
        while delta > list_length:
            delta = delta - list_length

        # case 1 positive and (value + idx) is less than (len(list) - idx) - straight move right
        if delta + idx <= list_length - idx:  # need to test
            # new_list[delta + idx] = num
            new_idx = delta + idx
        # case 2 positive and (value + idx) is greater than (len(list) - idx) - need to wrap around to front of list
        else:
            # new index is 0 + (delta - (list_length - idx))
            # new_list[delta - (list_length - idx)] = num
            new_idx = delta - (list_length - idx)

        for i, _ in range(new_idx, list_length):
            # shift these 1 way or the other?
            pass


    else:
        while abs(delta) > list_length:
            delta = delta + list_length

        # case 3 negative and (idx - abs(value)) is greater than 0 - straight move left
        if idx - abs(delta) >= 0:
            new_list[idx - abs(delta)] = num
        # case 4 negative and (idx - abs(value)) is less than 0 - need to wrap around to back of list
        else:
            # "decrease" delta by difference between 0 and num, i.e. idx, and then python's negative index
            # will take care of "wrapping"
            new_list[idx + delta] = num

print(new_list)

# print(f'length: {len(nums)}')
# print(f'min: {min(nums)}')
# print(f'max: {max(nums)}')
