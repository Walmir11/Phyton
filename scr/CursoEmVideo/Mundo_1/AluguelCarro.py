distancia= float(input('Qual a distancia em Km percorrida pelo carro? '))
dias= float(input('Quantos dias o carro foi usado? '))
preco = (dias*60)+(0.15*distancia)
print('O total a pagar é de R${}'.format(preco))