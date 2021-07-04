# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    casos = int(input())

    for caso in range(casos):

        inicio = input()

        a1 = 0
        a2 = 0

        cont = 1

        loop = True

        while loop == True:

            if inicio[cont] == 'a':

                a1 += 1

                cont += 1

            else:

                loop = False
        
        loop = True

        cont += 3

        while loop == True:

            if inicio[cont] == 'a':

                a2 += 1

                cont += 1

            else:

                loop = False

        print("k", end= '')

        for a in range(a1*a2):

            print("a", end='')

        print('')




