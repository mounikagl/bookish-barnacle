#include <stdio.h>

typedef union 
{
    int Integer;
    float RealNumber;
    char word;

}OneThingOrAnother;

int main()
{
    printf("int %d\n", (int) sizeof(int));
    printf("float %d\n", (int) sizeof(float));
    printf("char %d\n", (int) sizeof(char));
    printf("aggregate %d\n", (int) sizeof(OneThingOrAnother));
    return 0;
}
