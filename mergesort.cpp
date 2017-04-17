#include <stdio.h>
#include <stdlib.h>

void merge (int *a, int n, int m) {
  int i, j, k;
  int *x = (int*)malloc(n * sizeof (int));

  for (i = 0, j = m, k = 0; k < n; k++) {
    x[k] = j == n      ? a[i++]
         : i == m      ? a[j++]
         : a[j] < a[i] ? a[j++]
         :               a[i++];
  }

  for (i = 0; i < n; i++) {
    a[i] = x[i];
  }

  free(x);
}

void mergesort (int *A, int n) {
  if (n < 2)
    return;
  int m = n / 2;
  mergesort(A, m);
  mergesort(A + m, n - m);
  merge(A, n, m);
}

void printVector(int *v, int n) {
  for (int i = 0; i < n; i++) {
    printf("%d, ", v[i]);
  }
  printf("\n");
}

int main() {
  int A[20] = { 10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10 };
  mergesort(A, 19);
  printVector(A, 19);
  return 0;
}
