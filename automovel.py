from veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self,marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor
        
    def inprimirInformacoes(self):
        Veiculo.inprimirInformacoes(self)
        print("potenciaDoMotor: ", self.potenciaDoMotor)
