import random


n1 = (input('Digite o nome1: '))
n2 = (input('Digite o nome2: '))
n3 = (input('Digite o nome3: '))
n4 = (input('Digite o nome4: '))

Lista = [n1,n2,n3,n4]
random.shuffle(Lista)
print('A ordem de apresentação é: ')
print(Lista)