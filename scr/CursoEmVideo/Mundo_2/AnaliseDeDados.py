mais18 = 0
mulheresMenosDe20 = 0
homens = 0
while True:
    sexo = input('Qual é o seu sexo[M,F]: ').upper()
    idade = int(input('Qual é a sua idade: '))
    if idade > 18:
        mais18 += 1
    if sexo == 'F' and idade < 20:
        mulheresMenosDe20 += 1
    if sexo == 'M':
        homens += 1
    escolha = input('Deseja continuar[S,N]? ').upper()
    if escolha == 'N':
        print(f'----Fim do programa---- \nForam cadastrados {homens} homens 
              \nExiste {mais18} pessoas com mais de 18 anos 
              \nForam cadastradas {mulheresMenosDe20} mulheres com menos de 20 anos')
        break