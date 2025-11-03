class Animal:
    def __init__(self, numeros_patas):
        self.numero_patas = numeros_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join(f'{chave} {valor}' for chave, valor in self.__dict__.items() )}"
