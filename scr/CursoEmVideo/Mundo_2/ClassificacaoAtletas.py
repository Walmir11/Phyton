from datetime import date

atual = date.today().year
anoNasc = int(input("Digite seu ano de nascimento para classificalo: "))
idade = atual - anoNasc

if idade <= 9:
    print('Sua classificação é MIRIM!!')
elif idade <= 14:
    print('Sua classificação é INFANTIL!!')
elif idade <=19:
    print('Sua classificação é JÚNIOR!!')
elif idade <=25:
    print('Sua classificação é SÊNIOR!!')
else:
    print('Sua classificação é MASTER!!')