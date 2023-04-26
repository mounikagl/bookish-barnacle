#include <stdio.h>

int main()
{
    char message[] = "Hello world!";

    for (char *p = message; *p; ++p)
    {
        if (isupper(*p)) *p = (char) tolower(*p);
        else if (islower(*p)) *p = (char) toupper(*p);s
    }
    printf(message);
    
}