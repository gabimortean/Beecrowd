N = int(input())
print('%d' % N)

n100 = N // 100
N = N - n100 * 100


n50 = N // 50
N = N - n50 * 50


n20 = N // 20
N = N - n20 * 20


n10 = N // 10
N = N - n10 * 10


n5 = N // 5
N = N - n5 * 5


n2 = N // 2
N = N - n2 * 2

n1 = N // 1
N = N - n1 * 1

print('%d nota(s) de R$ 100,00' % n100)
print('%d nota(s) de R$ 50,00' % n50)
print('%d nota(s) de R$ 20,00' % n20)
print('%d nota(s) de R$ 10,00' % n10)
print('%d nota(s) de R$ 5,00' % n5)
print('%d nota(s) de R$ 2,00' % n2)
print('%d nota(s) de R$ 1,00' % n1)

