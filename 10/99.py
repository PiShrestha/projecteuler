import math
from functools import cmp_to_key

def compare(a: tuple, b: tuple) -> int:
    num1 = a[1] * math.log(a[0])
    num2 = b[1] * math.log(b[0])

    if num1 > num2:
        return 1
    elif num2 < num1:
        return -1
    else:
        return 0

greatest = (1, 1)
line_num = 0
with open('base_exp.txt', 'r') as file:
    nums = []
    for i, line in enumerate(file):
        line_stripped = line.strip().split(',')
        base = int(line_stripped[0])
        power = int(line_stripped[1])
        tup = (base, power)
        if compare(tup, greatest) == 1:
            greatest = tup
            line_num = i + 1

print(line_num)