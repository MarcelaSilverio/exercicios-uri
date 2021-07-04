# Autor: Marcela Prata Silverio
# Turma: INF3A

import math

if __name__ == "__main__":

    while True:

        numero = int(input())

        if numero == 0:

            break

        else:

            for linha in range(1, (numero+1)):

                for coluna in range(1, (numero+1)):

                    if coluna == 1:

                        print("%3d" % linha, end='')

                    elif linha == 1:

                        print(" %3d" % coluna, end='')

                    else:

                        print(" %3d" %
                              (int(math.fabs(coluna - linha) + 1)), end='')

                print('')

            print('')
