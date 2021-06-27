# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    num_paises = int(input())

    paises = []

    for numero in range(num_paises):

        nome, ouro, prata, bronze = input().split()

        pais = [nome, ouro, prata, bronze]

        paises.append(pais)

    paises.sort(key=lambda pais: pais[0])
    paises.sort(key=lambda pais: int(pais[3]), reverse=True)
    paises.sort(key=lambda pais: int(pais[2]), reverse=True)
    paises.sort(key=lambda pais: int(pais[1]), reverse=True)

    for pais in paises:

        print(f"{pais[0]} {pais[1]} {pais[2]} {pais[3]}")
