from datetime import datetime

Nasc = int(input('Qual seu ano de nascimento? '))
alf = input('Você é alfabetizado?[S/N] ').upper()[0]

def votacao(anoNasc, alfabetizacao):
    idade = datetime.now().year - anoNasc
    if 70 >= idade >= 18 and alfabetizacao == 'S':
        print(f'Você tem {idade} anos e a sua votação é OBRIGATÓRIA')
    elif 17 >= idade >= 16 or idade > 70 or alfabetizacao == 'N':
        print(f'Você tem {idade} anos e a sua votação é OPCIONAL')
    elif idade < 16:
        print(f'Você tem {idade} anos e a sua votação é INVALIDA')

votacao(Nasc,alf)
