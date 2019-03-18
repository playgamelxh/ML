# -*- coding: utf-8 -*-

a = [1, 2]
b = [3, 4]

c = zip(a, b)
print(c)

d = map(lambda (x, y): x + y, c)
print(d)


print([0.0 for _ in range(4)])
