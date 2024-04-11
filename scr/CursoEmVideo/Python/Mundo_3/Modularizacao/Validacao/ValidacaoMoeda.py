def validacao(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.')
        if entrada.replace('.', '', 1).isdigit():
            valido = True
            return float(entrada)
        else:
            print(f'Valor "{entrada}" inválido. Por favor, insira um número válido.')
        