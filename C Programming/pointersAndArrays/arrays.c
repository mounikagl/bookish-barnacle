#include <stdio.h>

int main()
{
    int num[3] = {1,2,3};
    int size = sizeof(num)/num[0];

    for(int i=0;i<3;++i)
    {
        printf("%d\n",num[i]);
    }
}
