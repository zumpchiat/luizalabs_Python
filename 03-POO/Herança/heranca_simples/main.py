from caminhao import Caminhao
from carro import Carro
from moto import Moto

moto1 = Moto("Black", "klh-2653", "2")
print(moto1)
moto1.ligar_motor()


print("=" * 100)
carro1 = Carro("Green", "poh-2773", "4")
print(carro1)
carro1.ligar_motor()
# carro1.acelerar()

print("=" * 100)
caminhao1 = Caminhao("Azul", "fgh-3344", "8", carregado=False)
print(caminhao1)
caminhao1.ligar_motor()
caminhao1.acelerar()
caminhao1.esta_carregado()
