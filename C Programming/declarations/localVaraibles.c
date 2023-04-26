#include <stdio.h>

void run()
{
    int pen;
    int pencil =3;

    pen += 1;
    pencil += 1;

    printf("pen = %d pencil = %d\n", pen, pencil);
}

int main()
{
    run();
    run();
    run();
    return 0;

}