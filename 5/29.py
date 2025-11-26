unique = set()

for a in range(2, 101):
    for b in range(2, 101):
        unique.add(pow(a, b))

print(len(unique))