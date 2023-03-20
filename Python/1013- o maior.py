x = input().split(" ")
a, b, c = x

maiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2

maior = (int(maiorAB) + int(c) + abs(int(maiorAB) - int(c))) / 2

print('%d eh o maior' % maior)

