valor = float(input('Digite o valor do Produto: '))
opcao = int(input('Digite o número correspondente a forma de pagamento: \n1-à vista dinheiro/cheque \n2-à vista no cartão \n3-2x no cartão \n4-3x ou mais no cartão \n'))

if(opcao == 1):
    valor = valor - valor * 0.10
    print('Desconto de 10%')
elif opcao == 2:
    valor = valor - valor * 0.05
    print('Desconto de 5%')
elif opcao == 3:
    parcela = valor/2
    print('Preço normal \nA parcela é de {}'.format(parcela))
elif opcao == 4:
    print('Juros de 20%')
    parcelamento = float(input('Digite a parcela: '))
    valor = valor + valor * 0.20
    parcela = valor/parcelamento
    print('Foi parcelado para {}x, o valor da parcela é de {}'.format(parcelamento,parcela))
else:
    print('Opção nãoi computada')

print('O valor a ser pago é {}'.format(valor))