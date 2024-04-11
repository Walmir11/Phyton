
num= int(input('Digite um número: '))
cont = 0

if(num>1):
    for c in range(1,num+1):
        if (num%c)==0:
            cont=cont+1

    if cont> 2:
        print("Não é primo")
    else:
        print('É primo')
else:
    print("O número tem que ser maior que 1")