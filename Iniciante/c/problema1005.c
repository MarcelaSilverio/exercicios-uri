// author: Marcela Prata Silverio

#include <stdio.h>

#define peso1 3.5
#define peso2 7.5

int main(){

    double nota1, nota2, media; //declaracao das variaveis double

    scanf("%lf", &nota1); //leitura da nota1
    scanf("%lf", &nota2); //leitura da nota2

    media = ((nota1 * peso1) + (nota2 * peso2))/(peso1+peso2); //calculo da media

    printf("MEDIA = %0.5lf\n", media); //impressao de dados

    return 0;

} 