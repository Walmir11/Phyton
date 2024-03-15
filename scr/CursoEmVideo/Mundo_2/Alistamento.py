from datetime import date


data = int(input('Digite o ano em que nasceu: '))
atual = date.today().year
idade = atual - data

print('Seu nascimento foi em {} tem {} no ano de {}'.format(data,idade,atual))

if idade == 18:
    print('Idade exata para alistamento militar obrigatório')
elif idade > 18:
    print('Idade maior que 18 para alistamento,está atrasado {} ano(s)'.format(idade-18))
else :
    print('Idade menor que 18 para alistamento, está adiantado {} ano(s)'.format(18-idade))