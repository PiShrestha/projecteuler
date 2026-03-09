rows = []

with open("18.txt", "r") as file:
    for line in file:
        raw_row = line.strip().split()
        int_row = [int(s) for s in raw_row]
        rows.append(int_row)
    
print(rows)

def child_index(index: int) -> (int, int):
    return (index, index + 1)

for i in range(len(rows) - 2, -1, -1):
    for j in range(0, len(rows[i])):
        left, right = child_index(j)[0], child_index(j)[1]
        rows[i][j] = rows[i][j] + max(rows[i+1][left], rows[i+1][right])

print(rows[0][0])
