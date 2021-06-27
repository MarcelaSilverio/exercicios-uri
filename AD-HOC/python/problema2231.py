# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    respostas = []

    caso = 0

    while True:

        num_medicoes, intervalo = [int(val) for val in input().split()]

        if num_medicoes == 0 or intervalo == 0:

            break

        else:

            caso += 1
            soma = 0

            maior_media = -100000
            menor_media = 100000 

            medicoes = []

            menos = -1

            entra = False

            for cont in range(num_medicoes):

                medida = int(input())
                medicoes.append(medida)

                soma += medida

                if menos != -1:

                    soma -= medicoes[menos]

                if cont == (intervalo-1):

                    entra = True
                

                if entra:

                    media = soma/intervalo

                    if media > maior_media:

                        maior_media = media

                    if media < menor_media:

                        menor_media = media

                    menos += 1

            print(f"Teste {caso}\n{int(menor_media)} {int(maior_media)}\n")

            

            

            




        

            
