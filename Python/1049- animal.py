n1 = input()
n2 = input()
n3 = input()

if n1 == 'vertebrado':
    if n2 == 'ave':
        if n3 == 'carnivoro':
            a = 'aguia'
        elif n3 == 'onivoro':
            a = 'pomba'
    elif n2 == 'mamifero':
        if n3 == 'onivoro':
            a = 'homem'
        elif n3 == 'herbivoro':
            a = 'vaca'

elif n1 == 'invertebrado':
    if n2 == 'inseto':
        if n3 == 'hematofago':
            a = 'pulga'
        elif n3 == 'herbivoro':
            a = 'lagarta'
    elif n2 == 'anelideo':
        if n3 == 'hematofago':
            a = 'sanguessuga'
        elif n3 == 'onivoro':
            a = 'minhoca'

print('{}'.format(a))

