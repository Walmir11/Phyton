salario = float(input('Digite seu salário: '))
if(salario>1250):
    salario=salario+(salario*0.10)
    print('Seu novo salário é {}'.format(salario))
else:
    salario=salario+(salario*0.15)
    print('Seu novo salário é {}'.format(salario))