#include<stdio.h>

float celcius_to_kelvin(celcius)
{
    return celcius +273.15f;
}

float celcius_to_fahrenhiet(celcius)
{
    return celcius*9/5+32;
}
int main()
{
    float celcius=0;
    while (celcius<100)
    {
        celcius = celcius+10;

        printf("%.2f C= %.2f K= %.2f F\n",
        celcius,
        celcius_to_kelvin(celcius),
        celcius_to_fahrenhiet(celcius));
    }
}