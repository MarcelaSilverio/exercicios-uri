# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    caso = 1 

    while True:

        num_jogadores = int(input())

        if num_jogadores == 0:

            break

        else:

            jogadores = []
            posicao = 1
            loop = 0

            for jogador in range(num_jogadores):

                nome = input()
                pontos = [int(val) for val in input().split(' ')]

                pontuacao = sum(pontos)

                pontuacao -= max(pontos)
                pontuacao -= min(pontos)

                jogadores.append([nome, pontuacao])

            jogadores.sort(key=lambda jogador: jogador[0])

            jogadores.sort(key=lambda jogador: int(jogador[1]), reverse=True)

            print(f"Teste {caso}")

            for numero, jogador in enumerate(jogadores):

                posicao = 1

                for cont in range(numero):

                    if jogadores[cont][1] > jogador[1]:

                        posicao += 1

                print(f"{posicao} {jogador[1]} {jogador[0]}")


            print('')

            caso += 1