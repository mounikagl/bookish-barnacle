#include <stdio.h>

typedef union
{
    int Integer;
    char Character;
} OneThingOrAnother;

typedef enum
{
    TheInteger,
    TheCharacter
} WhichThing;

int main()
{
    OneThingOrAnother var;
    var.Integer = 3;

    WhichThing type = TheInteger;

    printf("var %d type=%d\n", var.Integer, type);

    var.Character = 'V';
    type = TheCharacter;

    printf("var %c type=%d\n", var.Character, type);
    return 0;
}
