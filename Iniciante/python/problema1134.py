# Autor: Marcela Prata Silverio
# Turma: INF3A

if __name__ == "__main__":

    codigo = 0
    preferencias = [0, 0, 0]

    while codigo != 4:

        codigo = int(input())

        if (codigo > 0) and (codigo < 4):

            preferencias[codigo-1] += 1

    print("MUITO OBRIGADO")

    print(f"Alcool: {preferencias[0]}")
    print(f"Gasolina: {preferencias[1]}")
    print(f"Diesel: {preferencias[2]}")

        


