Lista = []

for c in range(0,7):
    num = int(input(f'Digite o {c+1}º número: '))
    Lista.append(num)

Lista.sort()
print('Os números pares são : ',end='')
for c in Lista:
    if c % 2 == 0:
        print(f'[{c}]', end='')
print()
print('Os números ímpares são : ',end='')
for c in Lista:
    if c % 2 != 0:
        print(f'[{c}]', end='')
