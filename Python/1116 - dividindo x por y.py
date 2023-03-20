n = int(input())
for i in range(n):
    a = input().split()
    x,y = a

    if int(y) == 0:
        print('divisao impossivel')
    else:
        div = int(x) / int(y)
        print('{:.1f}'.format(div))
