from ave import Ave
from mamifero import Mamifero


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, numeros_patas):
        super().__init__(cor_pelo, cor_bico, numeros_patas)
