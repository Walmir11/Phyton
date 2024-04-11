def fatorial(n,show=False):
    """
    Calculo de fatorial:
    N é o número a ser calculado
    show é opcional para mostrar o calculo
    return ele retorna o valor fatorial do número n
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f

print(fatorial(5,True))

help(fatorial)
