# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    TAMANHO = 100

    respostas = []

    for cont in range(TAMANHO):

        numero = float(input())

        if numero <= 10:

            respostas.append(f"A[{cont}] = {numero}")

    for resposta in respostas:

        print(resposta)

