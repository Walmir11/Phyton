produto = input('Qual o nome do produto? ')
preco = float(input('Qual o preço do produto? '))
if preco > 1000:
    produtos1000 += 1
produtoBarato = produto
menorPreco = preco
gasto = preco
produtos1000 = 0
while True:
    escolha = input('Deseja continuar[S,N]? ').upper()
    if escolha == 'N':
        print(f'----Fim do programa---- \nO produto mais barato foi {produtoBarato} \n{produtos1000} produtos custaram mais de 1000 \nO gasto total foi de R${gasto}')
        break
    produto = input('Qual o nome do produto? ')
    preco = float(input('Qual o preço do produto? '))
    gasto = gasto + preco
    if preco < menorPreco:
        produtoBarato = produto
        menorPreco = preco
    if preco > 1000:
        produtos1000 += 1
    