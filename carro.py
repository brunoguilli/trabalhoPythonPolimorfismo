from automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qtdPortas = qtdPortas
        
    def inprimirInformacoes(self):
        Automovel.inprimirInformacoes(self)
        print("qtdPortas: ", self.qtdPortas)
