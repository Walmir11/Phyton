from Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, cor, num_rodas, modelo, passageiros):
        super().__init__(cor, num_rodas, modelo)
        self.passageiros = passageiros

    def ComPassageiros(self):
        print('Sim' if self.passageiros else 'não está carregado')
