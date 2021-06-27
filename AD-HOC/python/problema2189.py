# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    caso = 0

    while True:

        convidados = int(input())

        if convidados == 0:

            break

        else:

            caso += 1

            ordem = input().split(' ')

            for convidado in ordem:

                if int(convidado) == (ordem.index(convidado)+1):

                    print(f"Teste {caso}\n{int(convidado)}\n")
                    
                    break
