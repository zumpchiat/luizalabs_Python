from veiculo import Veiculo


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):

        super().__init__(
            cor,
            placa,
            numero_rodas,
        )
        self.carregado = carregado

    def acelerar(self):
        print("acelerando..........")

    def esta_carregado(self):

        print(f"{'sim ' if self.carregado else 'Não' } está carrregado...")
