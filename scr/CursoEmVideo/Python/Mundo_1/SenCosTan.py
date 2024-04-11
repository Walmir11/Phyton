import math

angulo = float(input("digite um ângulo: "))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O cosseno é {}, o seno é {} e a tangente é {}'.format(cosseno,seno,tangente))
