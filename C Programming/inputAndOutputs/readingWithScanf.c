#include <stdio.h>

// int main()
// {
//     int a, b, c;
//     scanf("%d %d %d", &a, &b, &c);

//     printf("%d %d %d", a, b, c);
// }

int main()
{
    char message[10];
    scanf("%9s", message, sizeof(message));

    printf("%s\n", message);
}