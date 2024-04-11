time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy)
    while True:
        opcao = input('Quer continuar? [S/N]').upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break
print('-'*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qualjogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogaodr com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}: ')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('-'*40)
        print('VOLTE SEMPRE')
        