from sympy import primerange
import math

prime_numbers = set(primerange(6, 1000000))
freq = {}

num_circular_primes = 3 # start with {2, 3, 5}
num_of_rotations = {}

# with repetitions
def find_permutations(num_in_str: str) -> int:
    freq = {}
    for char in num_in_str:
        freq[char] = freq.get(char, 0) + 1
    
    denominator = 1
    for f in freq:
        denominator *= math.factorial(freq[f])

    numerator = math.factorial(len(num_in_str))
    return int(numerator / denominator)

def rotate_digits(num: int) -> set:
    ''' given an integer, it returns all rotations of the digits '''
    rotated_num = set()
    num_in_str = str(num)
    curr = num_in_str
    rotated_num.add(num)
    
    for i in range(len(num_in_str) - 1):
        curr = curr[1:] + curr[0]
        rotated_num.add(int(curr))

    return rotated_num

visited = set()

for num in prime_numbers:
    if num in visited:
        continue
    num_in_str = str(num)
    if '0' in num_in_str or '2' in num_in_str or '4' in num_in_str or '5' in num_in_str or '6' in num_in_str or '8' in num_in_str:
        continue

    freq[num_in_str] = freq.get(num_in_str, 0) + 1

    rotated_nums = rotate_digits(num)
    count = 0
    for n in rotated_nums:
        if n not in prime_numbers:
            break
        print(n)
        count += 1
        visited.add(n)
    
    if count == len(rotated_nums):
        num_circular_primes += count

    # # if the num is monodigit (meaning number consisting of only one digit), then it is circular
    # if num_in_str[0] == num_in_str[-1]:
    #     num_circular_primes += 1
    #     continue

print(num_circular_primes)