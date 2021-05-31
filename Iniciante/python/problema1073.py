#Autor: Marcela Prata Silverio
#Turma: INF3A

if __name__ == "__main__":

    n = int(input()) #leitura da variavel n

    for valor in range(2, n+1, 2): #percorre os valores pares de 1 a n

            print(f"{valor}^2 = {valor**2}") #apresenta o quadrado do valor