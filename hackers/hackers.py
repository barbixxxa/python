#! /bin/python3

import classes


def compile():
    fila = []

    qtd_portal = int(input('Quantidade de Portal: '))
    for i in range(qtd_portal):
        fila.append(classes.Portal())

    qtd_aparicao = int(input('Quantidade de Aparicao: '))
    for i in range(qtd_aparicao):
        fila.append(classes.Aparicao())

    qtd_acesso = int(input('Quantidade de Acesso: '))
    for i in range(qtd_acesso):
        fila.append(classes.Acesso())

    qtd_kraken = int(input('Quantidade de Kraken: '))
    for i in range(qtd_kraken):
        fila.append(classes.Kraken())

    qtd_ariete = int(input('Quantidade de Ariete: '))
    for i in range(qtd_ariete):
        fila.append(classes.Ariete())

    qtd_worms = int(input('Quantidade de Worms: '))
    for i in range(qtd_worms):
        fila.append(classes.Worms())

    qtd_parasita = int(input('Quantidade de Parasita: '))
    for i in range(qtd_parasita):
        fila.append(classes.Parasita())

    qtd_maniaco = int(input('Quantidade de Maniaco: '))
    for i in range(qtd_maniaco):
        fila.append(classes.Maniaco())

    qtd_raio = int(input('Quantidade de Raio: '))
    for i in range(qtd_raio):
        fila.append(classes.Raio())

    qtd_protetor = int(input('Quantidade de Protetor: '))
    for i in range(qtd_protetor):
        fila.append(classes.Protetor())

    qtd_explosao = int(input('Quantidade de Explosao: '))
    for i in range(qtd_explosao):
        fila.append(classes.Explosao())

    qtd_muralha = int(input('Quantidade de Muralha: '))
    for i in range(qtd_muralha):
        fila.append(classes.Muralha())

    qtd_shuriken = int(input('Quantidade de Shuriken: '))
    for i in range(qtd_shuriken):
        fila.append(classes.Shuriken())

    qtd_canhao = int(input('Quantidade de Canhao: '))
    for i in range(qtd_canhao):
        fila.append(classes.Canhao())

    for x, y in classes.calcular(fila).items():
        print(f"{x}: {y}")


if __name__ == "__main__":
    compile()
