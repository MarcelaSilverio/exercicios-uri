#Autor: Marcela Prata Silvério
#Turma: INF3A

import math

def calcula_delta(a, b, c):
    """Calcula o valor de delta.

    Essa função calcula o valor de delta através
    dos parâmetros a(float), b(float) e c(float) passados. O seu retorno
    consiste de um valor de ponto flutuante.
    """

    delta = (b ** 2) - 4 * a * c #calcula o valor

    return delta #retorna o valor de delta

def calcula_raizes(a, b, delta):
    """Calcula as raízes de função de segundo grau.

    Essa função calcula os dois possíveis valores de raízes
    de uma função de segundo grau através dos parâmetros
    a(float), b(float) e delta(float). O seu retorno consiste em uma tupla
    contendo os resultados.
    """

    raiz_1 = (- b + math.sqrt(delta)) / (2 * a) #calculo da primeira raiz
    raiz_2 = (- b - math.sqrt(delta)) / (2 * a) #calculo da segunda raiz

    raizes = (raiz_1, raiz_2) #tupla que contem ambos os valores

    return raizes #retorno das raizes


if __name__ == "__main__":

    a, b, c = input().split(" ") #leitura dos valores

    a = float(a) #conversao do valor
    b = float(b) #conversao do valor
    c = float(c) #conversao do valor

    delta = calcula_delta(a, b, c) #chama a função para calcular o valor de delta

    if delta < 0 or a == 0: #(raiz de numero negativo) ou (divisão por zero)

        print('Impossivel calcular') 

    else: #não existe impedimento para o cálculo das raízes
        
        raizes = calcula_raizes(a, b, delta) #chama a função para calcular as raízes

        print('R1 = %.5f' % raizes[0]) #impressão da primeira raíz
        print('R2 = %.5f' % raizes[1]) #impressão da segundo raíz