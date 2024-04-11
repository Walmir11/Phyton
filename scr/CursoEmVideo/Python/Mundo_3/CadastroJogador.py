jogador = {}

jogador['Nome do jogador'] = input('Digite seu nome: ')
jogador['Total de Partidas'] = int(input("Digite a quantidade de partidas: "))
totalGols = 0
if jogador['Total de Partidas'] > 0 :
    for c in range(0,jogador['Total de Partidas']):
        jogador[f'Partida {c+1}'] = int(input(f'Digite a quantidade de gols feitos na {c+1}ª partida: '))
        totalGols = jogador[f'Partida {c+1}'] + totalGols

print('-='*15)
for k,v in jogador.items():
    print(f'{k} = {v}')

print(f'O total de gols feitos foi {totalGols}')
        

