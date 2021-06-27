# Autor: Marcela Prata Silverio
# Turma: INF3A

if __name__ == "__main__":

    x = int(input())
    y = int(input())

    if x > y:

        troca = x
        x = y
        y = troca

    valores = []

    for valor in range((x+1), y):

        if (valor % 5 == 2) or (valor % 5 == 3):

            valores.append(valor)

    
    valores.sort()

    for valor in valores:

        print(valor)
