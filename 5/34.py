import math
from functools import reduce

print(7 * math.factorial(9)) # 2540160
print(8 * math.factorial(9)) # 2903040
# any 8 or more digits number > max possible sum (9!)

# Precompute factorials
digit_fact = [math.factorial(i) for i in range(10)]

# Upper bound = 7 * 9!
upper_bound = 7 * digit_fact[9]

curious = []

for num in range(10, upper_bound):
    if num == sum(digit_fact[int(d)] for d in str(num)):
        curious.append(num)

print(curious)
print("Sum:", sum(curious))