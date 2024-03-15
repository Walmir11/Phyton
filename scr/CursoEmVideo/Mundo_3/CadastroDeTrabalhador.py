from datetime import datetime
trabalhador = {}

trabalhador['nome'] = input('Digite seu nome: ')
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = datetime.now().year - anoNasc
trabalhador['idade'] = idade
trabalhador['Cateira de trabalho'] = float(input('Digite sua carteira de trabalho(Digite 0 caso não tenha): '))
if trabalhador['Cateira de trabalho'] != 0:
    trabalhador['Ano de contratação'] = float(input('Digite seu ano de contratação: '))
    trabalhador['Salario'] = float(input('Digite seu salário: '))
    trabalhador['Aposentadoria'] = trabalhador['idade'] + ((trabalhador['Ano de contratação'] + 35) - datetime.now().year)

print('-='*15)

for k,v in trabalhador.items():
    print(f'{k} : {v}')
