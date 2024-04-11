print('Digite 6 números')
soma = 0
for c in range(1,7):
    num = int(input('número {}: '.format(c)))
    if (num%2)==0:
        soma += num

print('A soma dos números pares é {}'.format(soma))