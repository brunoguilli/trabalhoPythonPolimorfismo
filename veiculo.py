class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade = None ):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0

    def inprimirInformacoes(self):
        print("Marca: ", self.marca)
        print("qtdRodas: ", self.qtdRodas)
        print("modelo: ", self.modelo)
        print("velocidade: ", self.velocidade)
    
    def acelerar(self, velocidadeAtual):
        self.velocidade += velocidadeAtual
    
    def frear(self, velocidadeAtual):
        self.velocidade -= velocidadeAtual