# Autor: Marcela Prata Silverio
# Turma: INF3A


if __name__ == "__main__":

    alunos, sorteado = [int(val) for val in input().split()]

    ordem = []
  
    for aluno in range(alunos):

        nome = input()
        ordem.append(nome)

    ordem.sort()

    print(ordem[sorteado-1])






            
