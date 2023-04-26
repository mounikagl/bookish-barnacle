#include <stdio.h>

int main()
{
    char *font = "Mounika Reddy";
    int size = 32;
    char * message = "Hello world";

    char buffer[500];

    sprintf(buffer, "<html><body><p style ='font-family:%s;font-s:ize:%dpx'>%s</p></body></html>",
    font,
    size,
    message);
    printf("%s\n", buffer);
}