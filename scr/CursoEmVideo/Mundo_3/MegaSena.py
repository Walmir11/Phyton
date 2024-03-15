from random import randint
from time import sleep
lista = []
jogos = []
qtd = 0
print('-'*30)
print('       JOGA NA MEGA SENA       ')
print('-'*30)
qtd = int(input('Quantos jogos vai querer sortear? '))

for c in range(0,qtd):
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
        if len(lista) >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print('-='*3,f'SORTEANDO {qtd} jOGOS','-='*3)
for c in range(0,qtd):
    print(f'O jogo {c+1} foi: {jogos[c]}')