listaUnica = []
repetidos = []
cont = 0
opcao = 'S'

while True:
    if opcao == 'N':
        break
    else:
        n = int(input(f'Digite o número na posição {cont}: '))
        if n not in listaUnica:
            listaUnica.append(n)
            print('Dado adicionado com sucesso!!')
            opcao = input('Deseja continuar?[S/N]').upper()
            cont+=1
        else:
            repetidos.append(n)
            print('O dado era repetido!!')
            opcao = input('Deseja continuar?[S/N]').upper()

listaUnica.sort()
print(f'Os dados em ordem crescente foram {listaUnica}')
print(f'Os dados adicionados repetidamente foram {repetidos}')
