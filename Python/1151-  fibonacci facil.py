n = int(input())
a = 0
b = 1

for i in range(n):
    if i != n-1:
        print(a, end=' ')
    else:
        print(a)
    c = a + b
    a = b
    b = c

