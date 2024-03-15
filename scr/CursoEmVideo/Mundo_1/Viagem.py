distancia = float(input('Digite a distância em km da viagem: '))
if(distancia<=200):
    valorTotal = distancia*0.50
    print('O valor a ser pago é {:.2f}'.format(valorTotal))
else:
    valorTotal = distancia*0.45
    print('O valor a ser pago é {:.2f}'.format(valorTotal))
