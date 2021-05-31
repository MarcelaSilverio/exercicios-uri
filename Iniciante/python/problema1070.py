#Autor: Marcela Prata Silverio
#Turma: INF3A

if __name__ == "__main__":

    x = int(input()) #leitura do valor x

    if x % 2 == 0: #se for par

        for valor in range(x+1, x+12, 2): #imprime seis valores a partir do próximo
            print(valor)

    else:
        
        for valor in range(x, x+12, 2): #imprime seis valores a partir de x
            print(valor)