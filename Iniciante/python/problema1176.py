# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    casos = int(input())

    sequencia = []
    respostas = []

    for cont in range(61):

        if cont == 0:
            numero = 0

        elif cont == 1:
            numero = 1

        else:
            numero = sequencia[cont-2] + sequencia[cont-1]

        sequencia.append(numero)

    for caso in range(casos):

        posicao = int(input())
        respostas.append(f"Fib({posicao}) = {sequencia[posicao]}")

    for resposta in respostas:

        print(resposta)