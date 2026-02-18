import math
from functools import reduce

res = math.factorial(100)
temp_res = res

res = str(res)

counter = {}

total = 0
while temp_res > 0:
    total += temp_res % 10
    temp_res = temp_res//10

for char in res:
    counter[char] = counter.get(char, 0) + 1

ans = reduce(lambda x, y: x + y, (map(lambda kv: int(kv[0]) * kv[1], counter.items())))
# ans = sum(map(lambda kv: int(kv[0]) * kv[1], counter.items()))

print(ans)

print(total)

