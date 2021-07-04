# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    while True:

        try:

            operacao = input().split("=")
            operandos = operacao[0].split("+")

            r = operandos[0]
            l = operandos[1]
            j = operacao[1]

            if not r.isdigit():

                print(int(j) - int(l))

            elif not l.isdigit():

                print(int(j) - int(r))

            elif not j.isdigit():

                print(int(r) + int(l))

        except EOFError:

            break
