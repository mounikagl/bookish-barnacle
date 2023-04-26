#include <stdio.h>

int main(void)
{
    int count=0;

    // for(count =0; count<10; count+=1)
    // for(;count<10; count+=1)
    for(;;)
    {
        printf("count=%d\n", count);
        count++;
        if (count == 10)
        {
            break;
        }
    }
    return 0;
}
