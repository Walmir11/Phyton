num = int(input('Digite um número para mostrar a tabuada dele: '))

for c in range(1,11):
    calculo = num*c
    print('{} X {} = {}'.format(num,c,calculo))