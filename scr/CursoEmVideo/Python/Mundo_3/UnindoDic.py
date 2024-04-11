Pessoa = {}
ListaP = []
ListaAc = []
cont = 0
mediaId = 0

while True:
    Pessoa['Nome'] = input('Digite seu nome: ')
    Pessoa['Sexo'] = input('Digite seu sexo: ')
    Pessoa['Idade'] = int(input('Digite sua idade: '))
    ListaP.append(Pessoa.copy())
    cont += 1 
    mediaId += Pessoa['Idade']
    opcao = input('Deseja continuar?[S/N] ').upper()
    if opcao == 'N':
        print('-='*15)
        print('     FIM DE CADASTRO     ')
        print('-='*15)
        break
calculoM = mediaId/cont

for c in ListaP:
    if Pessoa['Idade'] > calculoM:
        if Pessoa['Nome'] not in ListaAc:
            ListaAc.append(Pessoa['Nome'])

print(f'A quantidade de pessoas é {cont}')
print(f'A media de idade é {calculoM:.2f}')
print(f'As pessoas com idade acima da média são {ListaAc}')
    