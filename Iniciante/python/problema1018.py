#Autor: Marcela Prata Silverio
#Turma: INF3A

if __name__ == "__main__":

    notas = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0} #dicionario chave (nota) e valor (quantidade)

    valor = int(input()) #leitura do valor correspondente

    print(f'{valor}') #impressao do valor lido

    for nota, quantidade in notas.items(): #estrutura for iterando sobre o dicionario

        quantidade = valor // int(nota) #parte inteira da divisao
        valor %= int(nota) #resto da divisao

        print(f'{quantidade} nota(s) de R$ {nota},00') #impressao de dados


    