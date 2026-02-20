import math

smallest = 0
num = 100000
while(1):
    num_in_str = sorted(str(num))
    # 2x -- 6x
    for multiplier in range(2, 7):
        if num == 142857:
            print(multiplier, num, multiplier * num)
        if sorted(str(multiplier * num)) != num_in_str:
            break
    else:
        smallest = num
        break
    
    num += 1

print(smallest)