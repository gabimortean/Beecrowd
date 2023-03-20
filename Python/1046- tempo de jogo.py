i, f = map(int, input().split())

if i >= f:
    dur = (24 - i) + f
    print('O JOGO DUROU {} HORA(S)'.format(dur))

else:
    dur2 = f - i
    print('O JOGO DUROU {} HORA(S)'.format(dur2))
