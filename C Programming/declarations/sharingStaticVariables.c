#include <stdio.h>

static int books;

void up()
{
    books += 10;
    printf("books= %d\n", books);
}

void down()
{
    books -= 5;
    printf("books= %d\n", books);
}

int main()
{
    up();
    up();
    down();
    return 0;

}