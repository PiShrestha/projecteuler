import math

def find_digit(n) -> int:
    if n <= 9:
        return n
    
    nth = 9
    num = 9
    while nth <= n:
        num += 1
        nth += len(str(num))
        if nth == n:
            print("=", num)
            return int(str(num)[-1])

    print(num)
    return int(str(num)[n - nth - 1])

ans = 1

for i in range(7):
    ans *= find_digit(int(math.pow(10, i)))

print(ans)