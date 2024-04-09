def ValidacaoInt():
    inteiro = 0
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
            if isinstance(num,int):
                inteiro = num
                return inteiro
        except:
            print('ERRO, digite o número inteiro válido!!')

def ValidacaoReal():
    real = 0
    while True:
        try:
            num = float(input('Digite um número real: '))
            if isinstance(num,float):
                real = num
                return real
        except:
            print('ERRO, digite o número real válido!!')

print(f'O número inteiro foi {ValidacaoInt()}')
print(f'o número real foi {ValidacaoReal():.2f}')
