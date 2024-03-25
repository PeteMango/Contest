#include <bits/stdc++.h>
using namespace std;
const int MM = 1005;
int N, a[MM][MM], psa[MM][MM];
char s[MM];

int sum (int r1, int r2, int c1, int c2) {
  return psa[r2][c2] - psa[r1-1][c2] - psa[r2][c1-1] + psa[r1-1][c1-1];
}

int main() {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) {
    scanf(" %s", s+1);
    for(int j = 1; j <= N; j++) {
      a[i][j] = (s[j] == 'L');
    }
  }
  for(int i = 1; i <= N; i++) {
    if(a[1][i] == 1) {
      for(int j = 1; j <= N; j++) {
        a[j][i] ^= 1;
      }
    }
  }
  for(int i = 1; i <= N; i++) {
    if(a[i][1] == 1) {
      for(int j = 1; j <= N; j++) {
        a[i][j] ^= 1;
      }
    }
    for(int j = 1; j <= N; j++) {
      psa[i][j] = a[i][j] + psa[i-1][j] + psa[i][j-1] - psa[i-1][j-1];
    }
  }
  if(sum(2, N, 2, N) == 1) { // only one cell = 1
    for(int i = 1; i <= N; i++) {
      for(int j = 1; j <= N; j++) {
        if(a[i][j] == 1) {
          printf("%d %d\n", i, j);
          return 0;
        }
      }
    }
  }
  else if(sum(2, N, 2, N) == (N-1)*(N-1)) {
    printf("%d %d\n", 1, 1);
    return 0;
  }
  else if(sum(2, N, 2, N) == N-1) {
    for(int i = 1; i <= N; i++) {
      if(sum(i, i, 1, N) == N-1) {
        printf("%d %d\n", i, 1);
        return 0;
      }
      if(sum(1, N, i, i) == N-1) {
        printf("%d %d\n", 1, i);
        return 0;
      }
    }
  }
  printf("%d\n", -1);
}