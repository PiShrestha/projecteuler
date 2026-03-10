import math
from functools import reduce

def find_prime_numbers(upper_bound: int) -> set:
    answer = set()
    for num in range(1, upper_bound + 1):
        if isPrime(num): answer.add(num)
    return answer

def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    
    if num <= 3:
        return True
    
    if num %2 == 0:
        return False

    for divisor in range(3, int(math.sqrt(num)) + 1, 2):
        if num % divisor == 0:
            return False
        
    return True

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

# C(n,k) = (n!)/(k!(n-k)!) ->
# 10164 -> 2 + 1 + 1 + 2 + 4!/(2!*2!) = 6 + 12 = 18 
# print(find_all_prime_factors(2*2*3*7*11*11))

n = 100
# TOO LONG (need to check whether this works or not)
# while 1:
#     triangle_num = int(n*(n-1)/2)
#     factors = find_all_prime_factors(triangle_num)
#     divisor_with_same_prime = reduce(lambda x, y: x + y, 
#                                      map(lambda kv : kv[1], factors.items()))
#     num_unique_factors = len(factors)
#     num_divisors = 2 + math.factorial(num_unique_factors) / (2 * math.factorial(num_unique_factors - 2)) + divisor_with_same_prime
#     print(num_divisors)

#     if num_divisors > 500:
#         print(triangle_num)
#         break
    
#     n += 1

while 1:
    triangle_num = int(n*(n-1)/2)
    num_divisors = 0
    for i in range(1, int(math.sqrt(triangle_num) + 1)):
        if triangle_num % i == 0:
            num_divisors += 1
    
    print(num_divisors)
    if num_divisors > 250:
        break

    n += 1

print(triangle_num)
