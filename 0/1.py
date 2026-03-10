total_multiple3 = 0
total_multiple5 = 0
total_overlapping = 0

upper_bound = 1000

for num in range(3, upper_bound, 3):
    total_multiple3 += num

for num in range(5, upper_bound, 5):
    total_multiple5 += num

for num in range(15, upper_bound, 15):
    total_overlapping += num

final_total = total_multiple3 + total_multiple5 - total_overlapping
print(final_total)

'''
Info:
Sum=S3​+S5​−S15​
The formula for arithmetic sequences is Sn​=k/2(first term+last term).

The question states 'below 1000'. Therefore, 1000 is not one of the multiples.

995/5 = 199. So there are 199 multiples of 5 below 1000.
999/3 = 333. So there are 333 multiples of 3 below 1000.

Some numbers are multiples of both 3 and 5 (i.e. multiples of 15).
The last multiple of 15 below 1000 is 990.
990/15 = 66. So there are 66 multiples of 15.

Now using the formula:
Sum of multiples of 3 below 1000 -- Sum = 333(3 + 999)/2 = 166,833
Sum of multiples of 5 below 1000 -- Sum = 199(5 + 995)/2 = 99,500
Sum of multiples of 15 below 1000 -- Sum = 66(15 + 990)/2 = 33,165

(166,833 + 99,500) − 33,165 = 233,168

The final answer is 233,168.
'''