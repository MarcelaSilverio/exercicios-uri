// author: Marcela Prata Silverio

#include <stdio.h>
#include <math.h>

int main(){

    const double PI = 3.14159; //declaracao da constante PI
    double raio, area; //declaracao das variaveis double

    scanf("%lf", &raio); //leitura da variavel raio

    area = PI * pow(raio, 2); //calculo da area da circunferencia

    printf("A=%0.4lf\n", area); //impressao de dados

    return 0;

} 