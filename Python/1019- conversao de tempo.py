N = int(input())

hora = int(N // 3600)
N = N - hora * 3600

min = int(N / 60)
N = N - min * 60

seg = int(N - hora - min)
seg = N

print('{}:{}:{}'.format(hora, min, seg))