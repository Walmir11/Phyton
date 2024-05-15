class Veiculo:
    def __init__(self,cor,num_rodas,modelo):
        self.cor = cor
        self.num_rodas = num_rodas
        self.modelo = modelo

    def andando(self):
        print('O Veiculo está andando')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


