# Autor: Marcela Prata Silverio
#Turma: INF3A

if __name__ == "__main__":

    casos = int(input())

    numeros = []

    for caso in range(casos):

        numeros.append(input())
        numero = numeros[caso].split()
        numeros[caso] = (float(numero[0])*2 + float(numero[1])
                         * 3 + float(numero[2])*5)/10

    for resultado in numeros:
        print("%.1f" % resultado)
