# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    casos = int(input())
    respostas = []

    for caso in range(casos):
        
        numero = int(input())
        soma = 0
        divisor = numero

        while divisor != 1:

            divisor -= 1

            if numero % divisor == 0:

                soma += divisor

        if soma == numero:

            respostas.append(f"{numero} eh perfeito")
        
        else:

            respostas.append(f"{numero} nao eh perfeito")

    for resposta in respostas:

        print(resposta)





