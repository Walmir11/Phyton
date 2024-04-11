num = int(input('Digite um valor para iniciar: '))
razao = int(input('Digite a razão: '))
cont = 0
qtdTermos = 10

while qtdTermos != 0:
    while cont < qtdTermos:
        print(num, end='')
        print(' - 'if cont < qtdTermos-1 else ' - FIM ', end='')
        num = num + razao
        cont = cont + 1
    qtdTermos = int(input("\nQuantos termos vc quer mostrar a mais? "))
    cont = 0
print('Programa finalizado')