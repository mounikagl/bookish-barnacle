#include <stdio.h>

int main()
{
    int arr[ ] = {3,5,6,8,9,34,56,99};
    int n = sizeof(arr)/sizeof(arr[0]);
    int largest_num = 0;

    for(int i=0;i<n;i++)
    {
        if(arr[i]>largest_num)
        {
            largest_num = arr[i];
        }
    }
    printf("Largest num in array is :%d", largest_num);
    return 0;
}