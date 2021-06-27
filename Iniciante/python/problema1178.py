# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    valor = float(input())

    vetor = list(range(100))

    vetor[0] = valor

    for cont in range(1, len(vetor)):

        vetor[cont] = vetor[cont-1]/2

    for key, valor in enumerate(vetor):
        
        print("N[" + str(key) + "] = %.4f" % valor)



