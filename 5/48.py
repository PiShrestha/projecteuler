import math

# euclidean algorithm
def gcd(a: int, b: int):
    if a % b == 0 or b % a == 0:
        return min(a, b)
    
    c = max(a, b)
    d = min(a, b)

    while (c % d != 0):
        remainder = c % d
        c = d
        d = remainder

    return d 

def remainder(base:int, exponent:int, divisor: int):
    num = base

    for i in range(1, exponent):
        num *= base
        num = num % divisor

    return num

sum = 0
for num in range(1, 1001):
    sum += remainder(num, num, int(math.pow(10,10)))

print(sum % math.pow(10,10))
