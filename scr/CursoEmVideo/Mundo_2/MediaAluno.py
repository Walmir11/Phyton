nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2

if media >= 7:
    print('Sua média foi {} , está aprovado, parabéns !!!'.format(media)) 
elif media < 7 and media >= 5:
    print('Sua média foi {}, está de recuperação, estude !!!'.format(media))
else :
    print('Sua média foi {}, está reprovado, estude mais prox ano !!!'.format(media)) 