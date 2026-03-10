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

total = 2
curr_number = 3

# start from 3 because, checking only odd numbers reduces the execution time
start = time.time()
while curr_number < 2000000:
    if isPrime(curr_number):
        total += curr_number
    curr_number += 2

end = time.time()
print("total time:", end - start)

print(total)