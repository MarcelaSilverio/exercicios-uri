# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    notas = {'50': 0, '10': 0, '5': 0, '1': 0}
    respostas = []
    caso = 0
    string = ""


    while True:

        valor = int(input())

        if valor == 0:

            break

        else:

            loop = 0
            string = ""

            for nota, quantidade in notas.items():

                if loop != 0:

                   string += " "

                quantidade = valor // int(nota) 
                valor %= int(nota) 

                string += str(quantidade)

                loop += 1

            caso += 1

            respostas.append(f"Teste {caso}\n" + string + "\n")

    for resposta in respostas:

        print(resposta)







