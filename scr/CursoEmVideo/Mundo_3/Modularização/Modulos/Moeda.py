def resumo(num=0,taxa=0,moeda='R$'):
    dobro(num)
    metade(num)
    amumento10Porc(num,taxa)
    moeda1(num,moeda)
    
def dobro(num):
    dobro = num * 2
    print(f'O dobro do preço {moeda1(num)} é {moeda1(dobro)}')

def metade(num=0):
    medate = num /2
    print(f'A metade do preço {moeda1(num)} é {moeda1(medate)}')

def amumento10Porc(num,taxa):
    aumento = num + (num*taxa/100)
    print(f'O aumento de {taxa}% do preço {moeda1(num)} é {moeda1(aumento)}')

def moeda1(num, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')