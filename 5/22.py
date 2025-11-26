
with open("names.txt", "r") as file:
    for f in file:
        names = sorted(f.replace('"', '').split(","))

def calculate_value(s: str) -> int:
    total = 0
    for char in s:
        total += ord(char) - ord('A') + 1

    return total

ans = 0
for i, name in enumerate(names):
    ans += calculate_value(name) * (i + 1)

print(ans)