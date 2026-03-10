best = 0

for a in range(1, 100):
    value = 1
    for b in range(1, 100):
        value *= a
        s = sum(map(int, str(value)))
        best = max(best, s)

print(best)