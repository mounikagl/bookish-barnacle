#include <stdio.h>

void run()
{
    static int pen;
    static int pencil =3;

    pen += 1;
    pencil += 1;

    printf("pen = %d pencil = %d\n", pen, pencil);
}

void temp()
{
    int a =123;
    int b =456;
}

int main()
{
    run();
    run();
    run();
    // temp(); #only declared and not referenced the variables
    // temp();
    return 0;

}