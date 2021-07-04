# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    turma = 1 

    while True:

        num_alunos = int(input())

        if num_alunos == 0:

            break

        else:

            medias = {}
            loop = 0

            for aluno in range(num_alunos):

                codigo, media = [int(val) for val in input().split()]
                medias[codigo] = media

            maior_valor = medias[max(medias, key=medias.get)]

            print(f"Turma {turma}")
            
            for codigo, valor in medias.items():

                if valor == maior_valor: 
                    
                    print(codigo, end = ' ')

                    loop += 1

            print('\n')

            turma += 1


