#include <stdio.h>

int main()
{
    FILE * f = stdout;

    errno_t result = fopen_s(&f, "C:\\temp\\message.txt","W");

    if(result != 0)
    {
        char buffer[100];
        strerror_s(buffer, sizeof(buffer), result);

        printf("%s (%d)\n", buffer, result);
        return result;
    }
    fprintf_s(f, "Hello world\n");
    
    fclose(f);
}