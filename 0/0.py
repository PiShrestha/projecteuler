total = 0

first_n_numbers = 939000

for num in range(1, first_n_numbers, 2):
    total += num*num

print(total)