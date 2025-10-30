import math
import time

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

counter = 2
prime_number = 3
curr_number = 3

# start from 3 because, checking only odd numbers reduces the execution time
start = time.time()
while counter < 10001:
    curr_number += 2
    if isPrime(curr_number):
        prime_number = curr_number
        counter += 1

end = time.time()
print("total time:", end - start)

print(prime_number)