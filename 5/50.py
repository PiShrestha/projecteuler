import math
from functools import reduce

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

def find_prime_numbers(upper_bound: int) -> set:
    answer = set()
    for num in range(1, upper_bound + 1):
        if isPrime(num): answer.add(num)
    return answer

primes = find_prime_numbers(3943) # summing prime until 3943 is the smallest sum that is greater than 1000000

total = reduce(lambda x, y: x + y, primes)

primes_list = list(primes)
sorted_primes_list = sorted(primes_list)

window = len(sorted_primes_list) - 1
max_length = 0

while window > 0:
    total = reduce(lambda x, y: x + y, sorted_primes_list[:window])
    for right_index in range(window, len(sorted_primes_list)):
        right_prime = sorted_primes_list[right_index]
        left_prime = sorted_primes_list[right_index - window]
        total = total - left_prime + right_prime
        if isPrime(total) and total < 1000000:
            print(total, window, right_index)
            break
    if isPrime(total):
            break
    window -= 1


