# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    tamanho_vetor, minimo, maximo = [int(val) for val in input().split()]

    vetor = [int(val) for val in input().split()]

    resposta = 0

    for posicao1, numero_1 in enumerate(vetor):

        for posicao2, numero_2 in enumerate(vetor):

            if (posicao2 > posicao1):

                if (numero_1 + numero_2) >= minimo and (numero_1 + numero_2) <= maximo:

                    resposta += 1

    print(resposta)
