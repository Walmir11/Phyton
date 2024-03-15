print('Digite 999 para sair')
n = int(input('Digite o primeiro número: '))
soma = n
cont = 1

while n != 999:
    n = int(input('Digite outro número(999 para sair): '))
    if n != 999:
        soma += n
        cont+=1
print('Programa finalizado, A soma é {} e foram digitados {} números'.format(soma,cont))