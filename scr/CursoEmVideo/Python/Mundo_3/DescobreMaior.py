def descobreMaior(* num):
    numeros = []
    maior = cont = 0
    for c in num:
        numeros.append(c)
        if cont == 0:
            maior = c
        else:
            if c>maior:
               maior = c
        cont += 1
           

    
    print(f'Os números digitados {cont} números, foram {numeros}\nE o maior número foi {maior}')

descobreMaior(1,2,5,8,6,87)
descobreMaior(1,8)
descobreMaior(2,5,98)
