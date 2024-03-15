num1 = int(input('Digite o primeiro número'))
num2 = int(input('Digite o segundo número'))
num3 = int(input('Digite o terceiro número'))
if num1 > num2 and num1 > num3:
    print(num1, ' É o maior número')
elif num2 > num1 and num2 > num3:
    print(num2, ' É o maior número')
else:
    print(num3, ' É o maior número')