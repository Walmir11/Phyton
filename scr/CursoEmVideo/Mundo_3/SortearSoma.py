from random import randint

numeros = []

def sorteador():
    numeros.clear
    print('Sorteando 5 valores para uma lista...')
    print(f'Os números são ',end='')
    for c in range(0,6):
        num = randint(0,10)
        print(num,end=' ')
        numeros.append(num)
    print()

def soma(valores):
    soma = 0
    print(f'Os pares são ',end='')
    for c in numeros:
        if c%2==0:
            print(c,end=' ')
            soma = c + soma
    print(f'\nA soma deles é {soma}')

sorteador()
print('~'*40)
soma(numeros)
