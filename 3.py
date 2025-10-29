import math

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

# for i in range(100):
#     if isPrime(i): print(i)

def largestPrimeFactor(num: int) -> int:
    starting_odd_number = int(math.sqrt(num)) if int(math.sqrt(num)) % 2 != 0 else int(math.sqrt(num)) + 1 # always start with odd since even cannot be prime except for 2

    for divisor in range(starting_odd_number, 2, -2):
        if num % divisor == 0 and isPrime(divisor): return divisor

    return 2

print(largestPrimeFactor(600851475143))