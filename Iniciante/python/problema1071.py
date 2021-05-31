#Autor: Marcela Prata Silverio
#Turma: INF3A

if __name__ == "__main__":

    soma = 0 #variavel soma

    x = int(input()) #leitura do primeiro valor
    y = int(input()) #leitura do segundo valor

    if(x > y): #se o primeiro for maior que o segundo, troca
        aux = y
        y = x
        x = aux

    for valor in range(x+1, y, 1): #percorre os valores dentro do intervalo

        if valor % 2 != 0: #se for impar, soma

            soma += valor

    print(soma) #imprime a soma