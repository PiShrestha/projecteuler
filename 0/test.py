from collections import defaultdict
from functools import reduce

def add_all(*args) -> int:
    total = 0
    for arg in args:
        total += arg
    return total

def pi(*args) -> int:
    total = 1
    for arg in args:
        total *= arg
    return total

def calculate(func, *args):
    return func(*args)

print(calculate(pi, 1, 2, 3, 4))


class BookShelf:

    def __init__(self, qty: int):
        self.qty = qty

    def speak(self):
        print(self.qty)


b = BookShelf(3)
b.speak()

t = [1,2,3,4]
d = defaultdict(int)

a = reduce(lambda x, y : x + y, t)
print(a)

f = {1:4, 4:5, 3:1, 5:2, 6:4, 2:2}

sorted_f = {k: v for k, v in sorted(f.items(), key = lambda item: item[1])}
print(sorted_f)

data = {'d': 2, 'c': 1, 'a': 2, 'b': 3}

print(data.items())

# Sort the items and convert back to a dictionary
sorted_data_asc = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data_asc)
print(data)

w = [1,2,3,4,5,6]
g = w.copy()



w[4] = 100
print(g)
print(w)

