N = input().split(" ")
n1, n2, n3, n4 = N
n1 = float(n1) * 2
n2 = float(n2) * 3
n3 = float(n3) * 4
n4 = float(n4) * 1

media = (n1 + n2 + n3 + n4) / 10

print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')

if media < 5.0:
    print('Aluno reprovado.')

if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {:.1f}'.format(y))
    mediafinal = (y + media) / 2
    if mediafinal >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mediafinal))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(mediafinal))
