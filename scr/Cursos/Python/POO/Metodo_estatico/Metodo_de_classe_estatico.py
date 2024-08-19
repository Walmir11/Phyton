from datetime import datetime


class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_de_ano_nascimento(cls, ano, nome):
        ano_atual = datetime.now().year
        idade = ano_atual - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


# Funciona como uma fábrica
p = Pessoa.criar_apartir_de_ano_nascimento(2002, 'Walmir')
print(p.nome, p.idade)

print(Pessoa.e_maior_de_idade(p.idade))
print(Pessoa.e_maior_de_idade(15))
