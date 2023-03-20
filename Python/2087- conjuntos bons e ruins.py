def eh_bom_conjunto(palavras):
    palavras.sort()
    for i in range(len(palavras)-1):
        if palavras[i+1].startswith(palavras[i]):
            return 'Conjunto Ruim'
    return 'Conjunto Bom'


while True:
    lista=[]
    y = int(input()) # qtd de elementos da lista
    if y==0:
        break
    for i in range(y):
        a= input()
        lista.append(a)
    print(eh_bom_conjunto(lista))
