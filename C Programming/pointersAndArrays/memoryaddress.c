#include <stdio.h>

int main()
{
    int a = 1234;
    // printf("%p\n", &a);

    int *p = 0;
    p = &a;
    int j = * p;
    printf("a=%d p=%p j=%d", a , p, j);

    return 0;
}