#include <stdio.h>

int main() {
   int arr[50], size, i, j, temp;
   printf("Enter the size of the array: ");
   scanf("%d", &size);
   printf("Enter the elements of the array:\n");
   for(i = 0; i < size; i++) {
      scanf("%d", &arr[i]);
   }

   /* sorting the array using bubble sort */
   for(i = 0; i < size; i++) {
      for(j = i+1; j < size; j++) {
         if(arr[i] > arr[j]) {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
         }
      }
   }

   printf("The second smallest element is %d\n", arr[1]);

   return 0;
}
