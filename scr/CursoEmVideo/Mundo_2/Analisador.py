print('------ 1ª PESSOA --------')
nome = input('Nome: ')
idade = int(input('Idade: '))
sexo = str(input('M/F: '))
idadeV = idade
nomeV = nome

for c in range(2,5):
    print('------ {}ª PESSOA --------'.format(c))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: ').strip())
    sexo = str(input('M/F: ').strip())
    if idadeV < idade:
        idadeV = idade
        nomeV = nome

print('O mais velho(a) é {} com a idade de {}'.format(nomeV,idadeV))