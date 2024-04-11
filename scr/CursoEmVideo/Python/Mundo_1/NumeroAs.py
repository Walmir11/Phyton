frase = str(input('Digite uma frase: ')).upper().strip()
print('O numero de vezes que a letra A aparece é {}'.format(frase.count('A')))
print('O primeiro A aparece na posição {}'.format(frase.find('A')+1))
print('O último A aparece na posição {}'.format(frase.rfind('A')+1))