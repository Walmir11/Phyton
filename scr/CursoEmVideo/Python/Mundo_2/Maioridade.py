from datetime import date

contMaior = 0
contMenor = 0
dataAtual = date.today().year

for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if (dataAtual-ano) > 18:
        contMaior+=1
    else:
        contMenor+=1

print('Ao todo tem {} pessoas com maioridade'.format(contMaior))