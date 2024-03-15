cont = soma = 0
while True:
    n = int(input('Digite um número(Digite 999 para cancelar): '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'A quantidade de números foi: {cont} \nA Soma desses números foi: {soma}')