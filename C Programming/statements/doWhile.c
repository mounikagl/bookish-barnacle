#include <stdio.h>

int main()
{
    int count = 0;

    do
    {
        printf("count=%d\n", count);
        count += 1;
    }while (count<10);
    return 0;
}
