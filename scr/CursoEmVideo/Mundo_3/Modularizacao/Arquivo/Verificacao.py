from Menu.Menu import *

def arquivoExistente(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        arquivo = open(nome,'wt+')
        arquivo.close()
    except:
        print('Houve um problema ao criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for c in a:
            dado = c.split(';')   
            dado[1] = dado[1].replace('\n','')
            print(f'Nome: {dado[0]:<30} {dado[1]:>3} anos')   
    finally:
        a.close

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao adicionar um dado.')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # Escreve os dados no arquivo
        except:
            print('Ouve um problema ao adicionar os dados')
        else:        
            print(f'Novo registro de {nome} adicionado')
            a.close()
