from random import randint

sorteados = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior = 0
menor = sorteados[0]

for c in sorteados:
    if maior < c:
        maior = c
    if menor > c:
        menor = c

print(f'Os números sorteados foram {sorteados}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')