from datetime import datetime


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nacimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self._ano_nacimento
        return idade


#propertys são usados como set e get

pessoa = Pessoa('Walmir', 2002)
print(f'A pessoa tem o nome de {pessoa.nome} e a idade de {pessoa.idade}')
