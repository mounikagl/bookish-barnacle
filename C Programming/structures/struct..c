#include <stdio.h>

typedef struct 
{
    float x;
    float y;
}Pixel;

typedef unsigned char byte;

struct Color
{
    byte red;
    byte blue;
    byte green;
};

int main()
{
    Pixel p = {10.2f, 11.3f};
    struct Color c ={ 255, 128};

    float x = p.x;
    c.green = 255;
    printf("blue=%d green=%d red=%d\n", c.blue, c.green, c.red);

}