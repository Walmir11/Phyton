while True:
    num = int(input('Digite um número para que possa ser feito a tabuada dele(Digite um número negativo para encerrar o programa): '))
    if num < 0:
        print('Fim do programa')
        break
    print('-----TABUADA-----')
    for c in range(1,11):
        calculo = num * c
        print(f'{num} x {c} = {calculo}')
