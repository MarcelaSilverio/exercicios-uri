# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    while True:

        carnes = {}

        resposta = ""

        loop = 0

        try:

            quantidade = int(input())

            for cont in range(quantidade):

                carne, validade = input().split()

                carnes[carne] = int(validade)

            
            for carne in sorted(carnes, key = carnes.get):
                
                resposta += carne

                if loop != (quantidade-1):

                    resposta += " "

                loop += 1

            print(resposta)

        except EOFError:

            break



