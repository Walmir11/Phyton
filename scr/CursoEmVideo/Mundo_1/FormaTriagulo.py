print('Digite os 3 segmentos do triangulo!!')

seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))

if seg1< seg2+seg3 and seg2 < seg1+seg3 and seg3 < seg2+seg1:
    print('Esses segmentos formam um triangulo!!')

    if seg1 == seg2 == seg3:
        print('Esse triangulo é EQUILÁTERO')
    elif seg1 == seg2 or seg1 == seg3 or seg3 == seg2:
        print('Esse triângulo é ISÓSCELES')
    elif seg1 != seg2 and seg1 != seg3 and seg3 != seg2:
        print('Esse triângulo é ESCALENO')
else:
    print('Esses segmentos não formam um triângulo')

