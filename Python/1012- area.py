x = input().split(" ")
a, b, c = x

trian = (float(a) * float(c)) / 2
circ = (float(c) ** 2) * 3.14159
trap = ((float(a) + float(b)) * float(c)) / 2
quad = (float(b) ** 2)
retan = (float(a) * float(b))

print('TRIANGULO: %0.3f' % trian)
print('CIRCULO: %0.3f' % circ)
print('TRAPEZIO: %0.3f' % trap)
print('QUADRADO: %0.3f' % quad)
print('RETANGULO: %0.3f' % retan)
