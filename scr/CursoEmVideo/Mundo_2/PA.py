num = int(input('Digite um valor para iniciar: '))
razao = int(input('Digite a razão: '))
cont = 0

while cont != 10:
    print(num, end='')
    print(' - 'if cont < 9 else ' - FIM ', end='')
    num = num + razao
    cont = cont + 1