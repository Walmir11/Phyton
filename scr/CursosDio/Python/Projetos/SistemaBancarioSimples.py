menu='Informe a operação desejada: \n1-Depositar \n2-Sacar \n3-Extrato \n4-Sair \n'

saldo = 0
extrato = []
numeroSaques = 0

while True:
    opcao = int(input(menu))

    if opcao == 1:
        Deposito = float(input('Digite o valor do deposito: '))
        if Deposito>0:
            saldo += Deposito
            extrato.append(f'Deposito de R${Deposito:.2f} realizado')
            print(f'Deposito de R${Deposito:.2f} realizado')
        
    elif opcao == 2:
        print('Sacar')
        if saldo <= 0:
            print('Impossível fazer depósito com saldo no 0')
        else:
            saque = float(input('Digite o valor do saque: '))
            if saque>500:
                print('Limite do saque é 500')
            else:
                if numeroSaques == 3:
                    print('Seu limite de saque diário já foi ultrapassado!')
                else:
                    saldo -= saque
                    extrato.append(f'Saque de R${saque} foi realizado')
                    numeroSaques += 1
                    print(f'Saque de R${saque} foi realizado')

    elif opcao == 3:
        print('-'*40)
        print('EXTRATO'.center(40))
        print('-'*40)
        print(f'Saldo R${saldo}')
        for indice, acao in enumerate(extrato):
            print(f" {indice}- {acao}")

    elif opcao == 4:
        print('Saindo do programa, até mais tarde')
        break

    else:
        print('A opção selecionada não corresponde com as alternativas')
