from abc import ABC, abstractmethod, abstractproperty
from time import sleep
# ABC obriga que os metodos sejam implementados nas classes filhas

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando TV')
        sleep(1)
        print('Ligado')

    def desligar(self):
        print('Desligando TV')
        sleep(1)
        print('Desligado')

    def marca(self):
        return 'Samsung'


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando Ar Condicionado')
        sleep(1)
        print('Ligado')

    def desligar(self):
        print('Desligando Ar Condicionado')
        sleep(1)
        print('Desligado')

    def marca(self):
        return 'LG'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca())

controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca())
