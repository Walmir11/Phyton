vel = float(input('Digite sua velocidade: '))
if vel > 80:
    print('Velocidade acima do limite')
    multa = (vel-80)*7
    print('A multa é de R${}'.format(multa))

print('Tenha um bom dia!')