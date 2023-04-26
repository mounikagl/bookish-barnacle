#include <stdio.h>
#include <math.h>

int main()
{
    float a,b,c,discriminent,root1,root2;
    printf("Enter values of a b and c: ");
    scanf("%f %f %f", &a, &b, &c);

    discriminent = b*b - 4*a*c;

    if(discriminent>0)
    {
        root1 = -b + sqrt(discriminent)/2*a;
        root2 = -b - sqrt(discriminent)/2*a;
        printf("Roots are real and distinct root1=%.2f root2=%.2f", root1, root2);
    }else if(discriminent==0){
        root1=root2= -b/2*a;
        printf("Roots are ireal and equal %.2f", root1);
    }else{
        root1 = -b/2*a;
        root2 = sqrt(-discriminent)/2*a;
        printf("Roots are complex conjugates root1=%.2fi root2=%.2fj", root1, root2);
    }

    return 0;
}