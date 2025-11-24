import math
from sympy import primerange

def permutation(num: int) -> set:
    ''' given an integer, it returns all rotations of the digits '''
    rotated_num = set()
    num_in_str = str(num)
    curr = num_in_str
    rotated_num.add(num)
    
    for i in range(len(num_in_str) - 1):
        curr = curr[1:] + curr[0]
        rotated_num.add(int(curr))

    return rotated_num

def find_permutations(num_in_str: str) -> int:
    freq = {}
    for char in num_in_str:
        freq[char] = freq.get(char, 0) + 1
    
    denominator = 1
    for f in freq:
        denominator *= math.factorial(freq[f])

    numerator = math.factorial(len(num_in_str))
    return int(numerator / denominator)

four_digits_prime = list(primerange(1000, 10000))
freq = {}

for num in four_digits_prime:
    num_sorted_in_str = "".join(sorted(str(num)))
    freq[num_sorted_in_str] = freq.get(num_sorted_in_str, []) + [num]

candidates = []
for key, value in freq.items():
    if len(value) == 3:
        if value[2] - value[1] == value[1] - value[0]:
            print(value)
            continue
    if len(value) > 3:
        candidates.append(value)

def subset_3(nums: list) -> list:
    subset = []

    def dfs(i):
        if len(subset) == 3:
            pot = sorted(subset)
            if pot[2] - pot[1] == pot[1] - pot[0]:
                print(pot)
                return pot     # directly return the result
            return None

        if i >= len(nums):
            return None
        
        # include nums[i]
        subset.append(nums[i])
        ans = dfs(i + 1)
        if ans is not None:
            return ans

        # exclude nums[i]
        subset.pop()
        return dfs(i + 1)

    return dfs(0)


for candidate in candidates:
    subset_3(candidate)