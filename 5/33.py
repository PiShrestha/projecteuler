import math

fractions = []

def digit_cancelling(numerator: int, denominator: int) -> bool:
    original_fraction = numerator / denominator

    numerator_in_str = list(str(numerator))
    denominator_in_str = list(str(denominator))

    for n in numerator_in_str:
        if n in denominator_in_str:
            numerator_in_str.remove(n)
            denominator_in_str.remove(n)
            print(numerator_in_str, numerator)
            print(denominator_in_str, denominator)
            if int("".join(numerator_in_str)) / int("".join(denominator_in_str)) == original_fraction:
                return True
            else:
                return False



for i in range(12, 99):
    for j in range(i + 1, 99):
        if i % 10 == 0 or j % 10 == 0:
            continue
        if digit_cancelling(i, j):
            fractions.append((i, j))

num_prod = 1
den_prod = 1
for fraction in fractions:
    num_prod *= fraction[0]
    den_prod *= fraction[1]

print(num_prod)
print(den_prod)
print(fractions)

print(den_prod / math.gcd(num_prod, den_prod))