from random import randint


print('-'*50)
numAdv = randint(0,10)
acertou = False

while not acertou:
    num = int(input('Tente adivinhar o númeor que eu pensei entre 0 e 10: '))

    if num == numAdv:
        print('Você adivinhou o número, parabens!!')
        acertou = True
    else: 
        'Errouuuu, tente novamente: '

print('O número sorteado foi {} e não {}'.format(numAdv, num))