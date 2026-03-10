'''
c = sqrt(a^2 + b^2)
c = 1000 - (a + b)

1000 - (a + b) = sqrt(a^2 + b^2)
1000^2 - 2000(a + b) + a^2 + 2ab + b^2 = a^2 + b^2
1000^2 + 2ab = 2000a + 2000b
1000^2 = 2000a - 2ab +2000b
500000 = 1000a + 1000b - ab 
500000 + ab = 1000a + 1000b

500000 - 1000a = b(1000 - a)
(500000 - 1000a) / (1000 - a) = b
'''

a = 1

while 1:
    b = int((500000 - 1000 * a) / (1000 - a))
    remainder = (500000 - 1000 * a) % (1000 - a)
    if remainder == 0 :
        break
    a += 1

print("a:" , a , " , b:", b)

c = int((a**2 + b**2) ** 0.5)
print(c)

print("abc:", a*b*c)