# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    n = int(input())
    sequencia = []

    for cont in range(n):

        if cont == 0:
            numero = 0

        elif cont == 1:
            numero = 1

        else:
            numero = sequencia[cont-2] + sequencia[cont-1]
        
        sequencia.append(numero)

    print(' '.join(map(str, sequencia)))


        

