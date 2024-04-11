nome = str(input('Digite seu nome completo: '))
print('Seu último nome é {}'.format(nome[:nome.find(' ')]).strip())
print('Seu último nome é {}'.format(nome[nome.rfind(' '):]).strip())

##OU##

nome = str(input('Digite seu nome completo: '))
n = nome.split()
print('Seu último nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))