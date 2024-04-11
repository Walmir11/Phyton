sx = str(input('Digite seu sexo[M/F]: ').upper().strip)

while sx != 'M' or sx != 'F':
    if sx == 'M':
        print('Sexo masculino registrado com sucesso. ')
        break
    elif sx == 'F':
       print('Sexo femino registrado com sucesso. ')
       break
    else: 
        sx = input('Informação invalida, tente novamente: ').upper().strip