from random import randint


vitUsuario = 0
vitComp = 0
while True:
    if vitUsuario == 3:
        print('Parabéns, você venceu o jogo')
        break
    elif vitComp == 3:
        print('Você perdeu o jogo')
        break

    numComp = randint(0,10)
    escolha = input('Vamos jogar ímpar ou par, qual vc escolhe? ').upper()
    numUsuario = int(input('Digite seu número entre 0 e 10: '))

    if escolha == 'PAR':
        if (numUsuario + numComp) % 2 == 0:
            vitUsuario +=1
            print(f'Parabéns, vc venceu a rodada, está com {vitUsuario} vitórias')
        else:
            vitComp +=1
            print(f'Você perdeu a rodada, o computador jogou {numComp} e tem {vitComp} vitórias')

    if escolha == 'IMPAR':
        if (numUsuario + numComp) % 2 != 0:
            vitUsuario +=1
            print(f'Parabéns, vc venceu a rodada, está com {vitUsuario} vitórias')
        else:
            vitComp +=1
            print(f'Você perdeu a rodada, o computador  jogou {numComp} e tem {vitComp} vitórias')