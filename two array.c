#include <stdio.h>

int main() {
  int arr1[100], arr2[100], merged[200];
  int size1, size2, mergedSize, i, j;

  printf("Enter the size of the first array: ");
  scanf("%d", &size1);

  printf("Enter the elements of the first array: ");
  for(i=0; i<size1; i++) {
    scanf("%d", &arr1[i]);
  }

  printf("Enter the size of the second array: ");
  scanf("%d", &size2);

  printf("Enter the elements of the second array: ");
  for(i=0; i<size2; i++) {
    scanf("%d", &arr2[i]);
  }

  mergedSize = size1 + size2;

  // Merge the two arrays
  for(i=0; i<size1; i++) {
    merged[i] = arr1[i];
  }
  for(j=0; j<size2; j++) {
    merged[i+j] = arr2[j];
  }

  // Print the merged array
  printf("\nMerged array is: ");
  for(i=0; i<mergedSize; i++) {
    printf("%d ", merged[i]);
  }

  return 0;
}
