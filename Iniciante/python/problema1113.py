# Autor: Marcela Prata Silverio
# Turma: INF3A

if __name__ == "__main__":

    respostas = []

    while True:

        dupla = input().split()

        valores = [int(val) for val in dupla]

        if valores[0] == valores[1]:

            break

        elif valores[0] > valores[1]:

            respostas.append("Decrescente")

        else:

            respostas.append("Crescente")

    for resposta in respostas:

        print(resposta)