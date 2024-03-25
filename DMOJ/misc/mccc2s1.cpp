#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
int N, A[MAXN];

int main () {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) {
    scanf("%d", &A[i]);
  }
  sort(A+1, A+N+1);
  for(int i = 1; i <= N; i++) {
    printf("%d ", A[i]);
  }
}