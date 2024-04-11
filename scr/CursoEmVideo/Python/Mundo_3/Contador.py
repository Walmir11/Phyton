import time

for c in range(0,11):
    print(c,end=' ')
    #time.sleep(1)
print()
for c in range(10,-1,-2):
    print(c,end=' ')
    #time.sleep(1)
print()
print('Agora é sua vez de personalizar a contagem')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

def contador(ini, final, pas):
    if pas < 0:
        pas = abs(pas)
    if ini > final:
        while ini >= final:
            print(f'{ini}', end=' ')
            ini -= pas
    elif ini < final:
        while ini <= final:
            print(f'{ini}', end=' ')
            ini += pas
    else:
        print(f'{ini}', end=' ') 

contador(inicio,fim,passo)
