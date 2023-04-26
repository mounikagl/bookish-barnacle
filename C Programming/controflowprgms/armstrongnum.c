#include <stdio.h>
#include <math.h>

int isArmstrong(int num) {
    int temp, digit, sum = 0, n = 0;
    temp = num;
    while (temp != 0) {
        n++;
        temp /= 10;
    }
    temp = num;
    while (temp != 0) {
        digit = temp % 10;
        sum += pow(digit, n);
        temp /= 10;
    }
    if (num == sum) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int start, end, i;
    printf("Enter the start and end values: ");
    scanf("%d %d", &start, &end);
    printf("Armstrong numbers between %d and %d are: ", start, end);
    for (i = start; i <= end; i++) {
        if (isArmstrong(i)) {
            printf("%d, ", i);
        }
    }
    return 0;
}
