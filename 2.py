total = 2
prev_term = 1
curr_term = 2
upper_limit = 4000000

while curr_term < upper_limit:
    next_term = prev_term + curr_term
    if next_term % 2 == 0:
        total += next_term
    
    prev_term = curr_term
    curr_term = next_term

print(total)