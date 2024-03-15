lista  = ('Feijão',2.5,'Arroz', 3,'Açucar',2.35,'Farinha',3.55,'Carne',10.55)

print('-'*40)
print(f"{'LISTAGEM DE PRODUTOS':}")
print('-'*40)

for c in range(0,len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20}', end='')
    else:
        print(f'{lista[c]:.>20}')
