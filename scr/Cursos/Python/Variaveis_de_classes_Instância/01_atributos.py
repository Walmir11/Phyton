class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'


def mostrar_valores(*objts):
    for obj in objts:
        print(obj)


aluno1 = Estudante('Walmir', 5533)
aluno2 = Estudante('Jonas', 6565)
mostrar_valores(aluno1, aluno2)

Estudante.escola = 'Python'
aluno3 = Estudante('Charles', 9865)
mostrar_valores(aluno1, aluno2, aluno3)
aluno3.escola = 'Pycharm'
print(aluno3.__str__())
