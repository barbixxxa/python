#! /bin/python3

import datetime


class Ferramenta:
    def __init__(self, nome, espaco, tempo, preco):
        self.nome = nome
        self.espaco = espaco
        self.tempo = tempo*60
        self.preco = preco

    def __str__(self):
        return "--- %s --- \nEspaço em disco: %s \nTempo para compilar: %s \nPreço para compilar: %s" % (self.nome, self.espaco, self.tempo, self.preco)


class Portal(Ferramenta):
    def __init__(self):
        super().__init__(nome="Portal", espaco=10, tempo=20, preco=320)


class Aparicao(Ferramenta):
    def __init__(self):
        super().__init__(nome="Aparicao", espaco=5, tempo=15, preco=30)


class Acesso(Ferramenta):
    def __init__(self):
        super().__init__(nome="Acesso", espaco=1, tempo=1, preco=48)


class Kraken(Ferramenta):
    def __init__(self):
        super().__init__(nome="Kraken", espaco=7, tempo=8, preco=120)


class Ariete(Ferramenta):
    def __init__(self):
        super().__init__(nome="Ariete", espaco=5, tempo=10, preco=120)


class Worms(Ferramenta):
    def __init__(self):
        super().__init__(nome="Worms", espaco=3, tempo=1, preco=50)


class Parasita(Ferramenta):
    def __init__(self):
        super().__init__(nome="Parasita", espaco=3, tempo=0.3, preco=40)


class Maniaco(Ferramenta):
    def __init__(self):
        super().__init__(nome="Maniaco", espaco=15, tempo=30, preco=200)


class Raio(Ferramenta):
    def __init__(self):
        super().__init__(nome="Raio", espaco=6, tempo=8, preco=70)


class Protetor(Ferramenta):
    def __init__(self):
        super().__init__(nome="Protetor", espaco=4, tempo=5, preco=150)


class Explosao(Ferramenta):
    def __init__(self):
        super().__init__(nome="Explosao", espaco=6, tempo=5, preco=60)


class Muralha(Ferramenta):
    def __init__(self):
        super().__init__(nome="Muralha", espaco=2, tempo=2, preco=150)


class Shuriken(Ferramenta):
    def __init__(self):
        super().__init__(nome="Shuriken", espaco=1, tempo=0.3, preco=20)


class Canhao(Ferramenta):
    def __init__(self):
        super().__init__(nome="Canhao", espaco=1, tempo=0.2, preco=14)


def calcular(lista):

    retorno = {"Espaço": 0, "Tempo": 0, "Preço": 0}

    for i in lista:
        retorno["Espaço"] += i.espaco
        retorno["Tempo"] += i.tempo
        retorno["Preço"] += i.preco

        if (retorno.get(i.nome)):
            retorno[i.nome] += 1
        else:
            retorno[i.nome] = 1

    print(retorno["Tempo"])

    retorno["Tempo"] = str(datetime.timedelta(seconds=retorno["Tempo"]))

    return retorno


def print_classes():
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

    worms = Worms()
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


def get_calcular():
    lista = []

    lista.append(Portal())
    lista.append(Aparicao())

    print(calcular(lista))


def main():
    print_classes()
    get_calcular()


if __name__ == "__main__":
    main()
