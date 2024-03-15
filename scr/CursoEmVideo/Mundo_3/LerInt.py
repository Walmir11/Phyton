def LerInt(msg):
    ok = False
    valor = 0
    while True:
        num = input(msg)
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO, você não digitou o número corretamente!\033[m ')  
        if ok:
            break
    return valor

num = LerInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
