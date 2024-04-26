class Bicicleta:

    def __init__(self, modelo, cor, ano, valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('A bicicleta está buzinando!')

    def parar(self):
        print('A bicicleta está parada!')

    def correr(self):
        print('A bicicleta está correndo!')
