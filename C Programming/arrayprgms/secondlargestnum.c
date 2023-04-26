#include <stdio.h>

int main()
{
    int arr[ ] = {3,5,6,8,9,34,56,99};
    int n = sizeof(arr)/sizeof(arr[0]);
    int largest_num = 0;
    int second_largest;

    for(int i=0;i<n;i++)
    {
        if(arr[i]>largest_num)
        {
            largest_num = arr[i];
        }
    }
    for(int i=1; i<n; i++) {
        if(arr[i] > largest_num) {
            second_largest = largest_num;
            largest_num = arr[i];
        }
        else if(arr[i] > second_largest && arr[i] != largest_num) {
            second_largest = arr[i];
        }
    }

    printf("Second Largest num in array is :%d", second_largest);
    return 0;
}