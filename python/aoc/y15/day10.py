def encode(s):
    encoded_values = []
    previous_digit = s[0]
    current_run_length = 1

    for digit in s[1:]:
        if digit == previous_digit:
            current_run_length += 1
            previous_digit = digit
        else:
            encoded_values.append(str(current_run_length))
            encoded_values.append(previous_digit)

            previous_digit = digit
            current_run_length = 1

    encoded_values.append(str(current_run_length))
    encoded_values.append(previous_digit)

    return "".join(encoded_values)


value = "1321131112"

for _ in range(50):
    value = encode(value)

print(len(value))

