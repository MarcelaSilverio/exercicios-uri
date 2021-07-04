# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    num_predios = int(input())

    andares = [int(val) for val in input().split()]

    distancia_maior = 0

    #O predio de maior distancia do ultimo andar do predio 0
    for predio in range(num_predios):

        distancia = andares[0] + predio + andares[predio]

        if distancia > distancia_maior:

            distancia_maior = distancia

            predio_maior_distancia = predio

    distancia_maxima = 0
        
    #O amigo mais distante do ultimo andar do predio anterior    
    for predio in range(num_predios):

        if predio != predio_maior_distancia:

            distancia_maxima = max(distancia_maxima, andares[predio_maior_distancia] + abs( predio_maior_distancia - predio) + andares[predio])

    print(distancia_maxima)
    

        



