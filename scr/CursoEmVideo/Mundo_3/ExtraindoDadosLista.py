opcao = 'S'
lista = []

while True:
    if opcao == 'S':
        n = int(input('Digite um número: '))
        lista.append(n)
        opcao = input('Deseja continuar:[S/N] ').upper()
    else:
        print('Programa finalizado!')
        break

lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica {lista}')
print(f'A quantidade de números é : {len(lista)}')
if lista.count(5):
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')