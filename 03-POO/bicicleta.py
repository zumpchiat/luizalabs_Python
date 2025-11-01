class Bicicleta:

    def __init__(self, cor, ano, modelo, valor):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.valor = valor

    def parar(self):
        pass

    def correr(self):
        pass

    def buzinar(self):
        pass

    def __str__(self):
        return f"Class BICICLETA {self.__class__.__name__}: {", ".join(f'{chave} {valor}' for chave, valor in self.__dict__.items())} "


b1 = Bicicleta(cor="verde", ano="2016", modelo="caloi", valor=1000)

print(b1)
