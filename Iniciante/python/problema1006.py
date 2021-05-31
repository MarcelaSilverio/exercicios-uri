#Autor: Marcela Prata Silverio
#Turma: INF3A

if __name__ == "__main__":

    a = float(input()) #leitura da primeira nota
    b = float(input()) #leitura da segunda nota
    c = float(input()) #leitura da terceira nota

    media = ((a * 2) + (b * 3) + (c * 5)) / (10) #calculo da media ponderada

    print('MEDIA = %.1f' % media) #impressao da media
    