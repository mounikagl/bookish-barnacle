#include <stdio.h>

int main()
{
    int n;
    printf("Enter num:");
    scanf("%d", &n);

    if(n>0)
    {
        printf("Positive.");
    }else if(n<0){
        printf("Negative.");
    }else{
        printf("Number is Zero");
    }

    return 0;
}