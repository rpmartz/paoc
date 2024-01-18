from itertools import groupby

value = "1321131112"
num_iterations = 50

for _ in range(num_iterations):
    value = "".join([str(len(list(g))) + str(k) for k, g in groupby(value)])

print(len(value))
