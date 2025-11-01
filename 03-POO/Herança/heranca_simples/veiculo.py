class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numeros_rodas = numero_rodas

    def ligar_motor(self):
        print("Motor ligado...")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join(f'{chave} {valor}' for chave, valor in self.__dict__.items())}"
