# Autor: Marcela Prata Silverio
# Turma: INF3A

if __name__ == "__main__":

    maior = 0
    posicao_maior = 0

    for posicao in range(100):

        valor = int(input())
        if (valor > maior):
            maior = valor
            posicao_maior = posicao

    print(f"{maior}\n{posicao_maior+1}")
