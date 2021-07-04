# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    caso = 1 

    while True:

        num_depositos = int(input())

        if num_depositos == 0:

            break

        else:

            diferencas = []

            for deposito in range(num_depositos):

                joao, zezinho = [int(val) for val in input().split()]

                diferenca = joao - zezinho

                if deposito > 0:
                    
                    diferenca += diferencas[deposito-1]

                diferencas.append(diferenca)

            print(f"Teste {caso}")

            for diferenca in diferencas:

                print(diferenca)

            print('')

            caso += 1





