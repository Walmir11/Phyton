N = int(input())

# Para cada caso de teste
for _ in range(N):
    # Lê os valores A e B
    A, B = input().split()

    # Verifica se B corresponde aos últimos dígitos de A
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")
