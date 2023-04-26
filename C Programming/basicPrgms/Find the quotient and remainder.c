#include <stdio.h>

int main()
{
    int dividend = 99;
    int divisor = 3;

    int quotient = dividend/divisor;
    int remainder = dividend % divisor;

    printf("When %d divided by %d Quotient = %d and Remainder = %d", dividend , divisor, quotient, remainder);
    return 0;
}