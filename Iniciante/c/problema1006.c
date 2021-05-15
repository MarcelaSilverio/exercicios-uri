// author: Marcela Prata Silverio

#include <stdio.h>

#define peso1 2
#define peso2 3
#define peso3 5

int main(){

    double nota1, nota2, nota3, media; //declaracao das variaveis double

    scanf("%lf", &nota1); //leitura da primeira nota
    scanf("%lf", &nota2); //leitura da segunda nota
    scanf("%lf", &nota3); //leitura da terceira nota

    media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3))/(peso1 + peso2 + peso3); //calculo da media

    printf("MEDIA = %0.1lf\n", media); //impressao de dados

    return 0;

} 