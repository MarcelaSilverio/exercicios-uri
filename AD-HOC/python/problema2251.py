# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    caso = 1 

    while True:

        num_discos = int(input())

        if num_discos == 0:

            break

        else:

            print(f"Teste {caso}")

            print(f"{(2**num_discos)-1}\n")

            caso += 1

