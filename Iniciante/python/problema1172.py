# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    vetor = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for posicao in range(len(vetor)):

        numero = int(input())

        if (numero >= 1):
            
            vetor[posicao] = numero
    
    for posicao in range(len(vetor)):

        print(f"X[{posicao}] = {vetor[posicao]}")
