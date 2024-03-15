opcao = int(input('Escolha a operação para a conta: \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\n'))
print('Precisamos de dois números')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
calculo = 0

while opcao != 5:
    if opcao == 1:
        calculo = num1+num2
        print('O resultado da soma entre {} e {} é {}'.format(num1,num2,calculo))
    elif opcao == 2:
        calculo = num1*num2
        print('O resultado da multiplicação entre {} e {} é {}'.format(num1,num2,calculo))
    elif opcao == 4:
        print('Digite outros números')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opcao == 3:
        if num1>num2:
            print('O número maior é {}'.format(num1))
        else:
            print('O número maior é {}'.format(num2))

    opcao = int(input('Escolha outra opção: '))
    print('')

print("Programa finalizado!")
    