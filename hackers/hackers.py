#! /bin/python3

import classes


def create(qtd, tipo, qtd_total):
    if qtd == 0:
        return (0, qtd_total)
    for i in range(qtd):
        tool = classes.create_tool(tipo)
        qtd_total -= tool.espaco

    print(f"\n-> Espaço livre no disco: {qtd_total}\n")

    return (tool, qtd_total)


def compile():
    fila = []

    qtd_total = int(input('Espaço total no disco: '))

    qtd_tool = int(input('Quantidade de Portal: '))
    (tool, qtd_total) = create(qtd_tool, "Portal", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Aparicao: '))
    (tool, qtd_total) = create(qtd_tool, "Aparicao", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Acesso: '))
    (tool, qtd_total) = create(qtd_tool, "Acesso", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Kraken: '))
    (tool, qtd_total) = create(qtd_tool, "Kraken", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Ariete: '))
    (tool, qtd_total) = create(qtd_tool, "Ariete", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Worms: '))
    (tool, qtd_total) = create(qtd_tool, "Worms", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Parasita: '))
    (tool, qtd_total) = create(qtd_tool, "Parasita", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Maniaco: '))
    (tool, qtd_total) = create(qtd_tool, "Maniaco", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Raio: '))
    (tool, qtd_total) = create(qtd_tool, "Raio", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Protetor: '))
    (tool, qtd_total) = create(qtd_tool, "Protetor", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Explosao: '))
    (tool, qtd_total) = create(qtd_tool, "Explosao", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Muralha: '))
    (tool, qtd_total) = create(qtd_tool, "Muralha", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Shuriken: '))
    (tool, qtd_total) = create(qtd_tool, "Shuriken", qtd_total)
    fila.append(tool)

    qtd_tool = int(input('Quantidade de Canhao: '))
    (tool, qtd_total) = create(qtd_tool, "Canhao", qtd_total)
    fila.append(tool)

    for x, y in classes.calcular(fila).items():
        print(f"{x}: {y}")


if __name__ == "__main__":
    compile()
