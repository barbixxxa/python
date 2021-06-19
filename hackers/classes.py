#! /bin/python3

class Portal:
    def __init__(self, espaco=10, tempo=20, preco=320):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Aparicao:
    def __init__(self, espaco=5, tempo=15, preco=300):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Acesso:
    def __init__(self, espaco=1, tempo=1, preco=48):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Kraken:
    def __init__(self, espaco=7, tempo=8, preco=120):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Ariete:
    def __init__(self, espaco=5, tempo=10, preco=120):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Worms:
    def __init__(self, espaco=3, tempo=1, preco=50):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Parasita:
    def __init__(self, espaco=3, tempo=0.3, preco=40):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Maniaco:
    def __init__(self, espaco=15, tempo=30, preco=200):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Raio:
    def __init__(self, espaco=6, tempo=8, preco=70):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Protetor:
    def __init__(self, espaco=4, tempo=5, preco=150):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Explosao:
    def __init__(self, espaco=6, tempo=5, preco=60):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Muralha:
    def __init__(self, espaco=2, tempo=2, preco=150):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Shuriken:
    def __init__(self, espaco=1, tempo=0.3, preco=20):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


class Canhao:
    def __init__(self, espaco=1, tempo=0.2, preco=14):
        self.name = "Portal"
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.name, self.espaco, self.tempo, self.preco)


def test_classes():
    portal = Portal()
    print(portal)

    aparicao = Aparicao()
    print(aparicao)

    acesso = Acesso()
    print(acesso)

    kraken = Kraken()
    print(kraken)

    ariete = Ariete()
    print(ariete)

    worms = Aparicao()
    print(worms)

    parasita = Parasita()
    print(parasita)

    maniaco = Maniaco()
    print(maniaco)

    raio = Raio()
    print(raio)

    protetor = Protetor()
    print(protetor)

    explosao = Explosao()
    print(explosao)

    muralha = Muralha()
    print(muralha)

    shuriken = Shuriken()
    print(shuriken)

    canhao = Canhao()
    print(canhao)


if __name__ == "__main__":
    test_classes()
