# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    quant_criancas = int(input())

    positivo = 0
    negativo = 0

    nomes = []

    for crianca in range(quant_criancas):

        comportamento, nome = input().split()

        if comportamento == '+':

            positivo += 1

        else:

            negativo += 1

        nomes.append(nome)


    nomes.sort()

    for nome in nomes:

        print(nome)

    print(f"Se comportaram: {positivo} | Nao se comportaram: {negativo}")





