#include <stdio.h>

int main()
{
    int arr[ ] = {1,3,5,6,8,9,34,56,99};
    int n = sizeof(arr)/sizeof(arr[0]);
    int smallest_num;

    for(int i=0;i<n;i++)
    {
        if(arr[i]<smallest_num)
        {
            smallest_num = arr[i];
        }
    }
    printf("smallest num in array is :%d", smallest_num);
    return 0;
}