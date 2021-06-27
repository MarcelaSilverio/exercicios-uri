# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    casos = 0

    while True:

        partidas = int(input())

        vencedores = []

        if partidas == 0:

            break

        else:

            casos += 1

            par_nome = input()
            impar_nome = input()

            for partida in range(partidas):

                par_mao, impar_mao = [int(val) for val in input().split()]

                if (par_mao + impar_mao) % 2 == 0:

                    vencedores.append(par_nome)

                else:

                    vencedores.append(impar_nome)

            print(f"Teste {casos}") 
            
            for vencedor in vencedores:

                print(vencedor)

            print('')

            vencedores.clear()





            
