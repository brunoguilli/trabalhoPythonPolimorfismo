from bicicleta import Bicicleta
from carro import Carro

bike = Bicicleta("Bicilceta Caloi Barbie", 2, "Retrõ", None, 2, 1)
carro = Carro("Fiat", 4, "Argo", None, 1.3 , 4)


bike.acelerar(40)
bike.acelerar(10)
bike.inprimirInformacoes()
print("---------------------------")
carro.acelerar(100)
carro.frear(15)
carro.inprimirInformacoes()
