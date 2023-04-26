#include <stdio.h>

int main()
{
    int n, sum=0;
    printf("Enter positive integer: ");
    scanf("%d", &n);

    for(int i= 1;i<n+1;i++)
    {
        sum += i;
        // printf("Sum upto n is: %d\n", sum);
    }
    printf("Sum upto n is: %d", sum);
    return 0;
}