while True:
    x = int(input())
    if x != 0:
        par = 0
        for i in range(x, x + 10):
            if i % 2 == 0:
                par+=i
        print(par)
    else:
        break
