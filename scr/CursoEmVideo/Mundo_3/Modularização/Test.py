from Moeda import Moeda
from Validacao import ValidacaoMoeda

num = ValidacaoMoeda.validacao('Digite um número: ')

print('~'*25)
print('   INICIANDO CALCULOS')
print('~'*25)

Moeda.resumo(num,15,'USA')