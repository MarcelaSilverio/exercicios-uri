# Autor: Marcela Prata Silverio
# Turma: INF3A

import math

if __name__ == "__main__":

    while True:

        tamanho = int(input())

        if tamanho == 0:

            break

        else:

            linha_x = math.ceil(tamanho/2)
            coluna_x = linha_x

            ordem = ['direita', 'cima', 'esquerda', 'baixo']
            quantidade = 1
            posicao = 0
            troca = False
            loop = 0

            while (linha_x <= tamanho) and (coluna_x <= tamanho):

                for linha in range(1, tamanho+1):

                    for coluna in range(1, tamanho+1):

                        if (linha == linha_x) and (coluna == coluna_x):

                            print('X', end='')

                        else:

                            print('O', end='')

                    print('')

                print('@')

                if ordem[posicao] == 'direita':

                    coluna_x += 1

                elif ordem[posicao] == 'cima':

                    linha_x -= 1

                elif ordem[posicao] == 'esquerda':

                    coluna_x -= 1

                elif ordem[posicao] == 'baixo':

                    linha_x += 1

                loop += 1

                if loop == quantidade:

                    posicao += 1
                    loop = 0

                    if posicao > 3:

                        posicao = 0

                    if troca == True:

                        quantidade += 1
                        troca = False

                    else:

                        troca = True
