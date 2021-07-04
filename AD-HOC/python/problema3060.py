# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    valor = int(input())
    parcelas = int(input())

    resto = valor % parcelas

    for parcela in range(parcelas):

        if parcela < resto:

            print(int(valor/parcelas) + 1) 

        else:

            print(int(valor/parcelas))