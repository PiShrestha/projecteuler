import math

a = 20 # right moves
b = 20 # up moves

num_unique_moves = math.comb(a + b, a)

print(num_unique_moves)