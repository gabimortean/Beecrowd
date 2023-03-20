def troca_texto(txt, frase, tag):
    # print('entrei')
    frase_lo = frase.lower()
    txt_lo = txt.lower()
    while txt_lo in frase_lo:
        # print('entrou')
        pos = frase_lo.index(txt_lo)
        # print('index:',pos)#posicao do primeiro txt

        frase = list(frase)
        # print(frase)
        for j in range(pos, pos + len(txt)):
            frase.pop(pos)

            ##print(j,frase)
        # print(frase)
        for i, elemento in enumerate(tag):
            frase.insert(pos + i, elemento)
        frase = ''.join(frase)
        # print(frase)

        frase_lo = frase
        frase_lo = frase_lo.lower()
    return frase


'''
        frase_lo = frase_lo.replace(txt_lo, tag)
        #print('frase lo dps 1:',frase_lo)



        for j in range(pos,pos+len(txt)):
            frase[j]=frase_lo[j]

        frase = ''.join(frase)
        #print(frase_lo)
        #print(frase)


        '''

while True:
    try:
        txt = input()

        tag = input()
        frase = input()

        frasefinal = ''
        aux = ''

        dentro = False

        for letra in frase:

            if letra == '<':
                dentro = True

            if dentro:
                # print(letra)

                aux += letra
                # print('aux',aux)
            else:
                frasefinal += letra

            if letra == ">":
                dentro = False
                # aux+=letra

                aux = troca_texto(txt, aux, tag)
                if aux is None:
                    frasefinal += ''
                else:
                    frasefinal += aux
                aux = ''
        print(frasefinal)
    except EOFError:
        break
