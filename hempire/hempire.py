#4 cookies - 3 manteiga + 6 skunk
#4 torta - 3 farinha + 12 arabe
#4 donut - 3 marsh + 8 azul

#2 manteiga - 6 arabe
#2 farinha - 6 skunk
#2 marsh - 5 azul

class Manteiga:
    planta = 'arabe'
    quantidade = 6

    def __init__(self):
        print("manteiga")

    def getManteiga(self):
        return self.quantidade + self.planta

class Cookie:
    planta = 'skunk'
    pQuantidade = 6
    especial = Manteiga