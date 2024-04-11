dado = []
lista = []

while True:
    dado.append(input('Qual seu nome: '))
    num1 = float(input('Digite sua primeira nota: '))
    num2 = float(input('Digite sua segunda nota: '))
    media = (num1 + num2)/2
    dado.append(media)
    lista.append(dado[:])
    dado.clear()
    opcao = input('Deseja continuar?[S/N] ').upper()
    if opcao == 'N':
        break


print('-'*10,'BOLETIM','-'*10)
for c in lista:
    print(f'O nome do aluno é {c[0]} e sua média é {c[1]}')

