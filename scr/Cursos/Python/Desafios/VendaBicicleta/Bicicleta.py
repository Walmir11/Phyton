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
    #forma mais manual de imprimir os atributos de uma classe
    #def __str__(self):
        #return f'{self.__class__.__name__}: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'
    #Mais altomatizado caso queira adicionar atributos
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __del__(self):
        print('Removendo a instância da classe')
