print('Digite dois números para serem comparados')

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))

if(num1>num2):
    print('O número {} é maior do que o número {}'.format(num1,num2))
elif(num2>num1):
    print('O número {} é maior do que o númeor {}'.format(num2,num1))
else:
    print('Os dois números são iguais')
