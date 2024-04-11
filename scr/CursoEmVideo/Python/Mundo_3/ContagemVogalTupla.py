palavras = ('arnaldo','cesar','coelho','galvão','bueno')

for c in palavras:
    print(f'\nA palavra {c.upper()} tem as vogais ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')