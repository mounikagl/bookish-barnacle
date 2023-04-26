#include <stdio.h>
#include <ctype.h>

int main()
{
    char * message = "Hello world\r\nGoodDay";
    char * message = "Hello world\rGoodDay";
    char * message = "Hello world\tGoodDay\n";
    char * message = "\"Hello world\"\nC:\\Foo\\Bar\\nghttp://kennykerr.ca\n";
    printf(message);

}