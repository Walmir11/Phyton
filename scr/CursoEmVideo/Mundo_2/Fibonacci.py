n = int(input('Quantos números quer que apareça na tela? '))
cont = 0
f1 = 0
f2 = 1
f3 = 0

while cont < n:
    print(f1,end=' - 'if cont<n-1 else ' - FIM')
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    
    cont+=1
