# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    numero_supermercados = int(input())

    menor_valor = 1000000

    for supermercado in range(numero_supermercados):

        preco, gramas = [float(val) for val in input().split()]

        valor = (1000 * (preco/gramas))

        if valor < menor_valor:

            menor_valor = valor

    print("%0.2f" % menor_valor)
