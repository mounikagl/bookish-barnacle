#include <stdio.h>

int main() {
   int num, reversed_num = 0, remainder, original_num;

   printf("Enter an integer: ");
   scanf("%d", &num);

   original_num = num;

   // Reversing the integer
   while (num != 0) {
      remainder = num % 10;
      reversed_num = reversed_num * 10 + remainder;
      num /= 10;
   }

   // Checking if the reversed number is equal to the original number
   if (original_num == reversed_num)
      printf("%d is a palindrome.", original_num);
   else
      printf("%d is not a palindrome.", original_num);

   return 0;
}
