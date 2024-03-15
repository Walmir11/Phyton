print("Digite números para comparar e fazer a média: ")
num = int(input('Digite o 1º número: '))
maior = num
menor = num
soma = float (num) 
media = float (0) 
n = 1
escolha = input('Deseja continuar?[S/N] ').upper()

while escolha == 'S':
    n+=1
    num = int(input('Digite o {}º número: '.format(n)))
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    escolha = input('Deseja continuar?[S/N] ').upper()
media = soma/n
print('O maior número é {}, o menor é {} e a média é {}'.format(maior,menor,media))
