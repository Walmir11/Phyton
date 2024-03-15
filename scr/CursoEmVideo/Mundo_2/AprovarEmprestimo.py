casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanto é o seu salário? '))
anos = float(input('Quantos anos você vai pagar? '))

calculo = casa / (anos * 12)

print('O valor da casa é R$ {} ,a prestação vai ser de {:.2f} em {} anos '.format(casa,calculo,anos))

if calculo > salario*0.3:
    print("Emprestimo Negado")
else: 
    print('Emprestimo aprovado')