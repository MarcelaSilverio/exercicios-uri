# Autor: Marcela Prata Silverio
# Turma: INF3A

if __name__ == "__main__":

    soma = 0
    loop = 0
    status = 1

    while status == 1:

        if loop == 2:

            print("media = %.2f" % (soma/2))

            status = 3

            while (status != 1) and (status != 2):

                print("novo calculo (1-sim 2-nao)")

                status = int(input())

            if status == 1:
                
                loop = 0
                soma = 0

        else:

            nota = float(input())

            if nota >= 0 and nota <= 10:

                soma += nota
                loop += 1

            else:

                print("nota invalida")
