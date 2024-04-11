num= int(input('Digite o número a ser fatorado: '))
fatorial = 0
aux = num
print('Calculando {}! = '.format(aux), end='')
while aux != 0:
    print(aux, end='')
    print(' x ' if aux > 1 else ' = ', end='')
    fatorial = aux * (aux-1)
    aux=aux-1

print('{}'.format(fatorial))
