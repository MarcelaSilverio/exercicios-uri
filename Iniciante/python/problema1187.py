# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    TAMANHO = 12

    operacao = input()

    resultado = 0
    quantidade = 0

    for linha in range(TAMANHO):

        for coluna in range(TAMANHO):

            posicao = float(input())

            if (coluna > linha) and (coluna < (TAMANHO - (linha + 1))):

                resultado += posicao
                quantidade += 1

    if operacao == 'S':

        print("%.1f" % resultado)

    else:

        print("%.1f" % (resultado/quantidade))

