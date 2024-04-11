dado = []
lista = []
mai = men = 0

while True: 
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))
    if len(lista) == 0:
        men = mai = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    lista.append(dado[:])
    dado.clear()
    opcao = input('Deseja continuar:[S/N] ').upper()
    if opcao == 'N':
        print('Programa finalizado!')
        break

print(f'A quantidade de pessoas foi {len(lista)}')
print(f'O maior peso foi de {mai} KG, de ', end='')
for c in lista:
    if c[1] == mai:
        print(f'[{c[0]}]', end='')
print()
print(f'O menor peso foi de {men} KG, de ', end='')
for c in lista:
    if c[1] == men:
        print(f'[{c[0]}]',end='')
print()

