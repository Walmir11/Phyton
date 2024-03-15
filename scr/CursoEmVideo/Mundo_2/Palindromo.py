frase = str(input("Digite uma frase para saber se ela é um palindromo: ")).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto)-1,-1,-1):
    inverso += junto[c]
if inverso == junto:
    print('Esssa frase é um palíndromo')
else:
    print('Essa  frase não é um palíndromo')