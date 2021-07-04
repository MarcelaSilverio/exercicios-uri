# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    casos = int(input())

    for caso in range(casos):

        entrada = input()

        numero = '0'

        numeros = []

        for caracter in range(0, 13):

            if entrada[caracter].isdigit():

                numero += entrada[caracter]

            elif numero != '0':

                numeros.append(int(numero))

                numero = '0'

        if numero != '0':

            numeros.append(int(numero))

        print(sum(numeros))

        




