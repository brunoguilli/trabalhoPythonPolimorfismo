from veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        Veiculo.__init__(self,marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
 
    def inprimirInformacoes(self):
        Veiculo.inprimirInformacoes(self)
        print("numMarchas: ", self.numMarchas)
        print("bagageiro: ", self.bagageiro)
