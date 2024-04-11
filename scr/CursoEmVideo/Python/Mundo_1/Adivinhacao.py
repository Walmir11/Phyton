from random import randint


num = int(input('Tente adivinhar o númeor que eu pensei entre 0 e 5: '))
print('-'*50)
numAdv = randint(0,5)

if num == numAdv:
    print('Você adivinhou o número, parabens!!')
else:
    print('Mais sorte da próxiam vez  :( ')

print('O número sorteado foi {} e não {}'.format(numAdv, num))