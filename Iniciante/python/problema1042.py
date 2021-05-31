#Autor: Marcela Prata Silverio
#Turma: INF3A

if __name__ == "__main__":

    valores = input().split(" ") #leitura dos valores
    valores_ordenados = sorted(valores, key = lambda valor: float(valor)) #lista com os valores ordenados

    for valor in valores_ordenados: #imprime a lista ordenada
        print(valor)
    else: #ao final do interavel (nao ocorreu um break)
        print('')

    for valor in valores: #imprime a lista original
        print(valor)
