# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    caso = 0

    while True:

        n = int(input())
        papeis = 2

        if n == -1:

            break

        else:

            caso += 1

            if n != 0:
                
                for cont in range(n-1):
                    papeis *= 2

                papeis += 1

            print(f"Teste {caso}\n{papeis*papeis}\n")

