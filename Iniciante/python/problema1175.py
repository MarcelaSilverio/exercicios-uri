# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    TAMANHO = 20

    vetor = list(range(TAMANHO))

    for posicao in range((TAMANHO-1), -1, (-1)):

        vetor[posicao] = int(input())

    for key, numero in enumerate(vetor):
        
        print(f"N[{key}] = {numero}")
