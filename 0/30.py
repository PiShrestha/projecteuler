import math

print(6 * math.pow(9,5)) # 354294 [upper bound]
print(7 * math.pow(9,5)) # 413343 

mem = [i ** 5 for i in range(10)]

fifth_powers = []
for num in range(10, 354294 + 1):
    if num == sum([mem[int(d)] for d in str(num)]):
        fifth_powers.append(num)

print(fifth_powers)
print(sum(fifth_powers))