class Passaro:
    def voar(self):
        pass


class Pardal(Passaro):
    def voar(self):
        print("Pardal voando")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


def plano_voo(obj):
    obj.voar()
