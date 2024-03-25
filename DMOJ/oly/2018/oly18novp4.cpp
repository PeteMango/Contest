#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 5, MAXM = 17;
int N, M, A[MAXN], sT[MAXN][MAXM];

void build () {
  for(int i = 0; i < N; i++) {
    sT[i][0] = A[i];
  }
  for(int j = 1; (1<<j) <= N; j++) {
    for(int i = 0; (i + (1 << j) - 1) < N; i++) {
      if(sT[i][j - 1] > sT[i + (1 << (j - 1))][j - 1]) {
        sT[i][j] = sT[i][j - 1];
      }
      else {
        sT[i][j] = sT[i + (1 << (j - 1))][j - 1];
      }
    }
  }
}

int query (int L, int R) {
  int Lg2 = (int) log2(R-L+1);
  if (sT[L-1][Lg2] >= sT[R-1 - (1 << Lg2) + 1][Lg2]) 
        return sT[L-1][Lg2]; 
  
    else
        return sT[R-1 - (1 << Lg2) + 1][Lg2]; 
}

int main () {
  scanf("%d%d", &N, &M);
  for(int i = 0; i < N; i++) {
    scanf("%d", &A[i]);
  }
  build();
  for(int i = 0, L, R; i < M; i++) {
    scanf("%d%d", &L, &R);
    printf("%d\n", query(L, R));
  }
}