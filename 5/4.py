num_digits = 3
highest_palindrome = float('-inf')

def isPalindrome(num: int) -> bool:
    s = str(num)
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1
    
    return True

for i in range(10**num_digits, 10**(num_digits-1), -1):
    for j in range(i, 10**(num_digits-1), -1):
        product = i * j
        highest_palindrome = max(highest_palindrome, product) if isPalindrome(product) else highest_palindrome

print(highest_palindrome)
