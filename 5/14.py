
memoization = {1: 1}

def collatz_sequence(num: int) -> int:
    '''
    given a starting number, returns the number of terms leading to 1
    '''
    if num in memoization or num == 1:
        return memoization[num]
    
    next_num = 0
    if num % 2 == 0:
        next_num = int(num / 2)
    else:
        next_num = 3 * num + 1

    return 1 + collatz_sequence(next_num)

most = -1
max_n = 0
for num in range(1, 1000000):
    num_terms = collatz_sequence(num)
    memoization[num] = num_terms
    most = max(most, num_terms)
    max_n = num if most == num_terms else max_n

print(max_n)

