#include <stdio.h>

int main()
{
    int sum=0;
    int arr[10]={1,2,3,4,5,6,7,8,9};
    int n = sizeof(arr) / sizeof(arr[0]);

    for(int i=0; i<n; i++)
    {
        sum += arr[i];
    }
    printf("Sum of array elements is:%d \n", sum);
}