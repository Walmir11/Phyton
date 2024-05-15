from Funcoes import *

menu='Informe a operação desejada: \n1-Depositar \n2-Sacar \n3-Extrato \n4-Cria Usuario \n5-Criar Conta \n6-Listar Usuarios \n7-Sair \n'

while True:    
    opcao = int(input(menu))

    if opcao == 1:
        Deposito = float(input('Digite o valor do deposito: '))
        depositar(Deposito)

        
    elif opcao == 2:
        valor = float(input('Digite o valor do saque: '))
        sacar(saque=valor)

    elif opcao == 3:
        extrato()

    elif opcao == 4:
        nome = input('Digite seu nome: ')
        dtNasc = input('Digite sua data de nascimento: ')
        cpf = input('Digite seu CPF: ')
        endereco = input('Digite seu endereço: ')
        criarUsuario(nome,dtNasc,cpf,endereco)

    elif opcao == 5:
        usuarioCPF = input('Digite seu CPF: ')
        criarConta(usuarioCPF)

    elif opcao == 6:
        listar_contas()

    elif opcao == 7:
        print('Saindo do programa, até mais tarde...')
        break

    else:
        print('A opção selecionada não corresponde com as alternativas')