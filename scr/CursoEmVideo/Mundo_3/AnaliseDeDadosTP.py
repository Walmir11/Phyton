dados = (int(input('Digite o primeiro número: ')),int(input('Digite outro número: ')),
         int(input('Digite outro número: ')),int(input('Digite o último número: ')))
print(f'O número 9 apareceu {dados.count(9)} vezes')
if 3 in dados:
    print(f'O valor 3 apareceu {dados.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')
print('Números pares: ',end='')
for c in dados:
    if (int(c) % 2) == 0:
        print(c, end=', ')
        
