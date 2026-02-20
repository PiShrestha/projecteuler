import math

divisor = math.pow(10, 10)
first_ten = 10405071317 % divisor
total = first_ten

for i in range(11, 1001):
    total += math.pow(i, i) % divisor

print(total % divisor)