# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    n = int(input())
    valor = n
    cont = 1

    while (n - cont) != 1:

        valor *= (n - cont)

        cont += 1

    print(valor)
