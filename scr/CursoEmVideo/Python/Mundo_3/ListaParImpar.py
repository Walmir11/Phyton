pares = []
impares = []
lista = []
opcao = 'S'

while True:
    if opcao == 'S':
        n = int(input('Digite um número: '))
        lista.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
        opcao = input('Deseja continuar:[S/N] ').upper()
    else:
        print('Programa finalizado!')
        break

print('-'*40)
print(f'A lista completa: {lista}')
print(f'Os números ímpares: {impares}')
print(f"Os números pares: {pares}")
