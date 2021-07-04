# Autor: Marcela Prata Silverio
# Turma: INF3A

import math

if __name__ == "__main__":

    casos = int(input())

    for caso in range(casos):

        soma = 0

        num_linhas = int(input())

        for expoente in range(0, num_linhas):

            soma += 2**expoente

        print(soma)
