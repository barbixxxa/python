#! /bin/python3

import classes


def compile():
    fila = []
    print('--- Lista de Feramentas ---\n0 - Portal\n1 - Aparicao\n2 - Acesso\n3 - Kraken\n4 - Ariete\n5 - Worms\n6 - Parasita\n7 - Maniaco\n8 - Raio\n9 - Protetor\n10 - Explosao\n11 - Muralha\n12 - Shuriken\n13 - Canhao\n14 - Compilar')
    while True:
        try:
            item = int(input('O que você quer compilar?: '))
        except:
            print('Valor incorreto')
        else:
            if item == 0:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Portal())

            elif item == 1:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Aparicao())

            elif item == 2:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Acesso())

            elif item == 3:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Kraken())

            elif item == 4:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Ariete())

            elif item == 5:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Worms())

            elif item == 6:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Parasita())

            elif item == 7:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Maniaco())

            elif item == 8:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Raio())

            elif item == 9:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Protetor())

            elif item == 10:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Explosao())

            elif item == 11:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Muralha())

            elif item == 12:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Shuriken())

            elif item == 13:
                qtd = int(input('Quantos você quer compilar?: '))
                for i in range(qtd):
                    fila.append(classes.Canhao())

            elif item == 14:

                for x, y in classes.calcular(fila).items():
                    print(f"{x}: {y}")
                break

            else:
                print(fila)
                continue


if __name__ == "__main__":
    compile()
