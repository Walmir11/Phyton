num = int(input('Digite um número inteiro: '))
base = int(input('Para qual base vc deseja transformar: \n1-Binario \n2-Octal \n3-Hexadecimal \n'))

if base == 1 :
    n = bin(num)
    print('O num {} em binario é {}'.format(num,n[2:]))
elif base == 2:
    n = oct(num)
    print('O num {} em octal é {}'.format(num,n[2:]))
elif base == 3:
    n = hex(num)
    print('O num {} em hexadecimal é {}'.format(num,n[2:]))
else:
    print("A base não está catalogada:(")