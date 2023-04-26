#include <stdio.h>

typedef unsigned char byte;

int main()
{
    int i = 3;
    float f = 1.23f;
    double d = 12.345;
    char c = "c";

    unsigned int ui = 34u;
    short int si = 12;
    long int li = 1934;

    byte b = 0x12;

    printf("%d (%d)\n",i, (int) sizeof(int));

}