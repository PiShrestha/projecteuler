import string

with open("42.txt", "r") as f:
    for line in f:
        words = [word.strip('"') for word in line.split(",")]
        words = sorted(words, key = lambda x: len(x))

print(len(words[-1]))

print(len(words[-1]) * 26) # 364 [max value]

characters = string.ascii_uppercase
triangle_numbers = set()

num = 0
max_num = 0
while max_num < 365:
    triangle_numbers.add((num * (num + 1)) // 2)
    num += 1
    max_num = num

alphabet_position = {char: (i + 1) for i, char in enumerate(characters)}
print(alphabet_position)

counter = 0
for word in words:
    if sum(alphabet_position[char] for char in word) in triangle_numbers:
        counter += 1

print(counter)