matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = 0
somaP = 0
somaC = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite na linha {l+1} coluna {c+1}: '))
        if matriz[l][c]%2 == 0:
            somaP = somaP + matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[l][2]:
            somaC = somaC + matriz[l][2]

print('-'*30)
print('A matriz é: ')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]' , end='')
    print()

print(f'A soma de todos os pares é {somaP}')
print(f'A soma dos valores da terceira coluna é {somaC}')
print(f'O maior valor da segunda linha é {maior}')
