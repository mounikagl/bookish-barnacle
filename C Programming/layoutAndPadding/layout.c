#include <stdio.h>

typedef struct 
{
    short first;
    // int second;
    short third;// padding disapperars so layout takes sizeof 8 bytes shorts are aligned side to side
    int second; // before shorts are taking space for padding so 12 bytes is required

}layout;

int main()
{
    printf("short %d\n", (int) sizeof(short));
    printf("int %d\n", (int) sizeof(int));
    printf("sturct %d\n", (int) sizeof(layout));

    return 0;
}
