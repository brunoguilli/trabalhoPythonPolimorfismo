from automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica
        
    def inprimirInformacoes(self):
        Automovel.inprimirInformacoes(self)
        print("partidaEletrica: ", self.partidaEletrica)
