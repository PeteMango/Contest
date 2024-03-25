#include <bits/stdc++.h>
using namespace std;
const int MAXK = 15, MAXN = 25, MM = 105;
int K, N, CNT = 0, C[MAXK][MAXN], A[MM][MM];

int main () {
  scanf("%d %d", &K, &N);
  for(int i = 1; i <= K; i++) {
    for(int j = 1; j <= N; j++) {
      scanf("%d", &C[i][j]);
    }
  }
  for(int i = 1; i <= K; i++) {
    for(int j = 1; j < N; j++) {
      for(int k = j + 1; k <= N; k++) {
        A[C[i][j]][C[i][k]]++;
      }
    }
  }
  for(int i = 1; i < MM; i++) {
    for(int j = 1; j < MM; j++) {
      if(A[i][j] == K) {
        CNT++;
      }
    }
  }
  cout << CNT << endl;
}