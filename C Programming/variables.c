#include<stdio.h>
int main()
{
    float celcius, fahrenhiet,kelvin;

    celcius = 21;
    kelvin = celcius +273.15f;
    fahrenhiet = celcius*9/5+32;

    printf("%.2f C= %.2f K= %.2f F\n",
    celcius,
    kelvin,
    fahrenhiet);
}