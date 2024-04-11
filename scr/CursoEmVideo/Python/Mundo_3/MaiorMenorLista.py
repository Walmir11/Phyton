lista = []
posMa = []
posMe = []
maior=0
menor=0
for c in range(0,6):
    lista.append(int(input(f'Digite o número na posição {c}: ')))
    if c == 0 :
        maior = menor = list[c]
    if(lista[c] >= maior):
        maior = lista[c]
        posMa.append(c)
    if(lista[c] <= menor):
        menor = lista[c]
        posMe.append(c)

print(f'A lista digitada foi {lista}')
print(f'O maior número foi {maior} nas posições {posMa}')
print(f'O menor número foi {menor} nas posições {posMe}')