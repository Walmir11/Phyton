import math


print('Vamos calcular seu IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
calculo = peso / math.pow(altura,2)

print('Seu IMC foi {:.2f}'.format(calculo))

if calculo < 18.5:
    print('Está abaixo do peso!')
elif 18.5 <= calculo <25:
    print('Está no peso ideal!')
elif 25 <= calculo < 30:
    print('Está em sobrepeso!')
elif 30 <= calculo < 40:
    print('Está na obesidade!')
elif calculo > 40:
    print('Está em obesidade mórbida!!!')