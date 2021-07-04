# Autor: Marcela Prata Silverio
# Turma: INF3A

import math

if __name__ == "__main__":

    while True:

        acm = input()

        if acm == '0':

            break

        else:

            resultado = 0
            k = 1

            for digito in acm[::-1]:

                resultado += (int(digito) * math.factorial(k))

                k += 1

            print(resultado)
