def square_of_sum(num: int) -> int:
    sum_of_n_numbers = int(num*(num+1)/2)
    return sum_of_n_numbers**2

# 1, 5, 14, 30, 55, 91 ... (pretty random)

def sum_of_squares(num: int) -> int:
    answer = 0
    for n in range(1, num + 1):
        answer += n**2
    return answer

print(square_of_sum(100) - sum_of_squares(100))