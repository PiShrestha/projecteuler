from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from lib.prime import isPrime
from functools import reduce
from itertools import product

valid_first_digits = ['2' , '3' , '5', '7']
valid_middle_digits = ['1' , '3' , '7', '9']
valid_last_digits = ['3' , '7']

truncatable_primes = []
# two digits:
for first_digit in valid_first_digits:
    for last_digit in valid_last_digits:
        n = int(first_digit + last_digit)
        if isPrime(n):
            print(n)
            truncatable_primes.append(n)

def truncate(num: str) -> bool:
    # left to right
    i = 1
    for i in range(1, len(num)):
        if not isPrime(int(num[i:])):
            return False

    # right to left:    
    for i in range(1, len(num)):
        if not isPrime(int(num[:i])):
            return False

    return True

num_mid_digits = 1


while len(truncatable_primes) < 11:
    for first_digit in valid_first_digits:
        for mids in product(valid_middle_digits, repeat=num_mid_digits):
            for last_digit in valid_last_digits:
                n_str = first_digit + ''.join(mids) + last_digit
                n = int(n_str)

                if isPrime(n) and truncate(n_str):
                    truncatable_primes.append(n)
                    print(n, len(truncatable_primes))

    num_mid_digits += 1

print(truncatable_primes)
print(reduce(lambda x, y: x + y, truncatable_primes))

