#include <stdio.h>

int calcular_suma_descendente(int num)
{
    int k;
    int sumando;
    int suma;
    
    suma = num;
    k = 10;
    sumando = num % k;
    while (sumando != num)
    {
        suma += sumando;
        k *= 10;
        sumando = num % k;
    }
    return (suma);
}

int main(void)
{
    int num;
    int resultado;

    scanf(" %d", &num);
    while (num != 0)
    {
        resultado = calcular_suma_descendente(num);
        printf("%d\n", resultado);
        scanf(" %d", &num);
    }
}