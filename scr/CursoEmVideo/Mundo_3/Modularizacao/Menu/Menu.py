def ValidacaoInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('ERRO, digite um número inteiro válido!')
            continue
        else:
            return num


def linha(tam=42):
    return '-'*tam

def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu do Sistema')
    i = 1
    for c in lista:
        print(f'{i} - {c}')
        i += 1
    cabecalho('Digite a sua opcao')
    opc = ValidacaoInt('Digite um número inteiro: ')
    return opc