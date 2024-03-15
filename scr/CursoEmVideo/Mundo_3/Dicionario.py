aluno = {}
lista = []
abMedia = []
acMedia = []

while True:
    aluno['nome'] = str(input('Digite seu nome: '))
    aluno['media'] = float(input('Digite sua média: '))
    lista.append(aluno.copy())
    if aluno['media']>=6:
        acMedia.append(aluno['nome'])
    else:
        abMedia.append(aluno['nome']) 
    opcao = input('Deseja continuar?[S/N] ').upper()
    if opcao == 'N':
        break

for c in lista:
    print(f"Nome: {c['nome']}, Média: {c['media']:.2f}")
    
print(f'Os alunos abaixo da media são {abMedia}')
print(f'Os alunos acima da media são {acMedia}')
    