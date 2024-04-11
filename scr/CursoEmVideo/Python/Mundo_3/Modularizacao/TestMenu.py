from Menu.Menu import *
from Arquivo.Verificacao import *

arq = 'NomesPessoas.txt'

if not arquivoExistente(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = input('Nome: ')
        idade = ValidacaoInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print('ERRO, digite uma opção válida!')
