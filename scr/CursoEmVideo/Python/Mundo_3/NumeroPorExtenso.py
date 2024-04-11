numero = ('zero','um','dois','três', 'quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= num <=20:
        print(f'Você digitou o número {numero[num]}')
        break
    else:
        num = int(input('Número invalido. Digite um número entre 0 e 20: '))