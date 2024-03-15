peso = float(input('Peso da 1ª pessoa: '))
menorP = peso
maiorP = peso

for c in range(2,6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if(peso>maiorP):
        maiorP = peso
    elif peso<menorP:
        menorP = peso
    
print('O maior peso é {}'.format(maiorP))
print('E o menor peso é {}'.format(menorP))