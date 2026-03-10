n_by_n = 1001
num_iters = n_by_n//2

curr_num = 1
total = curr_num
jump = 2

for i in range(0, num_iters, 1):
    for j in range(4):
        curr_num += jump
        total += curr_num
    
    jump += 2

print(total)