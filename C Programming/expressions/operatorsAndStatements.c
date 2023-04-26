#include <stdio.h>

int main()
{
    int eggs = 48;
    // int dozen;
    int dozen = eggs/12;

    printf("dozen= %d\n", dozen);

    eggs--;
    printf("eggs= %d\n", eggs);
    
    eggs++;
    printf("eggs= %d\n", eggs);

    --eggs;
    printf("eggs= %d\n", eggs);

    ++eggs;
    printf("eggs= %d\n", eggs);
    return 0;
}
