saldo = 0
numeroSaques = 0
numConta = 1
historico = []
Pessoas = []
contas = []
listaPessoas = {}
listaContas = {}


def depositar(deposito, /):
    global numeroSaques
    global saldo
    if deposito > 0:
        saldo += deposito
        historico.append(f'Deposito de R${deposito:.2f} realizado')
        print(f'Deposito de R${deposito:.2f} realizado')
    else:
        print(f'Valor de deposito invalido!!')


def sacar(*, saque):
    global numeroSaques
    global saldo
    if saldo <= 0:
        print('Impossível fazer saque com saldo no zerado')
    else:
        if saque > 500:
            print('O limite é 500, tente um valor mais baixo')
        else:
            if numeroSaques == 3:
                print('Seu limite de saque diário já foi ultrapassado!')
            else:
                saldo -= saque
                historico.append(f'Saque de R${saque} foi realizado')
                numeroSaques += 1
                print(f'Saque de R${saque} foi realizado')


def extrato():
    print('=' * 40)
    print('EXTRATO'.center(40))
    print('=' * 40)
    print(f'Saldo R${saldo}')
    for indice, acao in enumerate(historico):
        print(f" {indice + 1}- {acao}")
    print('~' * 40)


def criarUsuario(nome, dtNasc, cpf, endereco):
    existe = False
    for pessoa in Pessoas:
        if pessoa["CPF"] == cpf:
            existe = True

    if not existe:
        listaPessoas['Nome'] = nome
        listaPessoas['Data de nascimento'] = dtNasc
        listaPessoas['CPF'] = cpf
        listaPessoas['Endereço'] = endereco
        Pessoas.append(listaPessoas.copy())
        print('Usuario criado com sucesso!')
    else:
        print('Usuario já existe')


def criarConta(usuarioCPF):
    listaContas['Agencia'] = '0001'
    listaContas['Número da conta'] = numConta
    for pessoa in Pessoas:
        if pessoa["CPF"] == usuarioCPF:
            listaContas['Usuario'] = pessoa['Nome']
    contas.append(listaContas.copy())
    print('Conta criada com sucesso!')


def listar_contas():
    for conta in contas:
        print(
            f"Agencia: {conta['Agencia']} \nNúmero da conta: {conta['Número da conta']} \nNome do Usuario: {conta['Usuario']}")
