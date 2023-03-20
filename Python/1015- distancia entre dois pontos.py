import math

p1 = input().split(" ")
p2 = input().split(" ")
x1, y1 = p1
x2, y2 = p2

valor = ((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)
dist = math.sqrt(valor)
print('%0.4f' % dist)
