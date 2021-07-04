# Autor: Marcela Prata Silverio
# Turma: INF3A

import math

if __name__ == "__main__":

    while True:

        

        try:

            angulo, distancia, altura = [float(val) for val in input().split()]

            arvore = ((math.tan(math.radians(angulo))) * distancia) + altura

            print("%0.2f" % (arvore * 5))

        except EOFError:

            break
