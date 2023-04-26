#include <stdio.h>

int main()
{
    int eggs =3;

    switch (eggs)
    {
    case 0:
        printf("No cake.\n");
        break;
    case 1:
        printf("Cup cake.\n");
        break;
    case 2:
        printf("Cake.\n");
        break;
    default:
        printf("Ice cake.\n");
        break;
    }
}