def respNotas(*notas, situacao=False):
    notas_dict = {}  # Inicializa um dicionário para armazenar as notas
    cont = soma = maior = menor = 0
    qtd = len(notas)

    for c in notas:
        cont += 1
        notas_dict[f'Nota-{cont}'] = c  # Adiciona a nota ao dicionário
        soma += c

        # Verifica a maior e a menor nota
        if cont == 1:
            maior = menor = c
        else:
            if c>maior:
               maior = c
            if c<menor:
                menor = c

    calculo = soma / qtd

    print(f'A maior nota foi {maior}')
    print(f'A menor nota foi {menor}')
    print(f'A média da turma foi {calculo:.2f}')
    print(f'A quantidade de notas foi {qtd}')

    if situacao:
        if calculo < 6:
            print('RUIM')
        elif 6 <= calculo < 7:
            print('RAZOÁVEL')
        else:
            print('BOM')

respNotas(5.5, 10, 2.6, 6, situacao=True)
    