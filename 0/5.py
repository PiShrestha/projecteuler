import math
from functools import reduce

prime_numbers = set()
upper_bound = 80

def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    
    if num <= 3:
        return True
    
    if num % 2 == 0:
        return False

    for divisor in range(3, int(math.sqrt(num)) + 1, 2):
        if num % divisor == 0:
            return False
        
    return True

def find_prime_numbers(upper_bound: int) -> set:
    answer = set()
    for num in range(1, upper_bound + 1):
        if isPrime(num): answer.add(num)
    return answer

prime_numbers = find_prime_numbers(upper_bound)

def find_all_prime_factors(num: int) -> dict:
    '''
    for a given number, return all the prime factors along with its frequency 
    for example: 288 -> {2:5, 3:2}
    '''
    if isPrime(num):
        return {1:1, num:1}
    
    factors = {}
    prime_numbers = find_prime_numbers(int(num**0.5) + 1)
    sqrt = int(num**0.5) + 1
    prime_numbers = list(prime_numbers)

    # factor = a x b where a ≤ sqrt(num) ≤ b
    while len(prime_numbers) != 0:
        potential_factor = prime_numbers.pop()
        counter = 0
        while num % potential_factor == 0:
            b = int(num/potential_factor)
            if b > int(num**0.5) and isPrime(b):
                factors[b] = factors.get(b, 0) + 1
            counter += 1
            num /= potential_factor
        if counter != 0:
            factors[potential_factor] = counter
    
    return factors

highest_num_factors = {}

for num in range(2, upper_bound + 1):
    prime_factors = find_all_prime_factors(num)
    for factor, freq in prime_factors.items():
        highest_num_factors[factor] = max(highest_num_factors.get(factor, freq), freq)
    
answer = reduce(
    lambda x, y: x * y,
    map(lambda kv: kv[0] ** kv[1], highest_num_factors.items())
)

print(highest_num_factors)
print(answer)


# Efficient answer using arithmetic
pn = find_prime_numbers(upper_bound)
product = reduce(lambda x, y : x * y, pn)

for n in pn:
    exp = int(math.log(upper_bound, n)) - 1
    if exp == 0:
        break
    product *= (n ** exp)

print(product)


# using LCM and GCD

def lcm(a, b):
    return a * b // math.gcd(a, b)

result = 1

for i in range(1, 21):
    result = lcm(result, i)
    print(result)

print(result)