from functools import reduce

def find_divisors(num: int) -> List[int]:
    divisors = []

    for divisor in range(1, int(num**0.5) + 1):
        if num % divisor == 0:
            pair = num // divisor
            
            if pair % 2 == 0 or divisor % 2 == 0:
                divisors.append(divisor)
                if pair != divisor and pair != num:
                    divisors.append(pair)

    return divisors

print(find_divisors(220))
print(find_divisors(284))

visited = set()
total = 0

for a in range(1, 100001):
    if a in visited:
        continue

    divisors_a = find_divisors(a)
    if not divisors_a:
        continue
    sum_divisors_a = reduce(lambda x, y: x + y, divisors_a)

    if sum_divisors_a > 10000 or sum_divisors_a in visited or a == sum_divisors_a:
        continue

    divisors_b = find_divisors(sum_divisors_a)
    if not divisors_b:
        continue
    sum_divisors_b = reduce(lambda x, y: x + y, divisors_b)

    visited.add(a)

    if sum_divisors_b == a:
        print("a, b: ", a , sum_divisors_a)
        total += a + sum_divisors_a

print(total)

