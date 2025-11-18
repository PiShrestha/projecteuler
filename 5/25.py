a = 1
b = 1
c = 0
n = 2

while (len(str(c)) != 1000):
    n += 1
    c = a + b
    a = b
    b = c

print(n)