#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MOD = 1e9 + 7, MAXK = 1e5 + 5;

int K, N;
ll CND[MAXK], DP[MAXK];

int main () {
  scanf("%d %d", &N, &K);
  DP[0] = 1;

  for(int i = 1, C; i <= N; i++) {
    scanf("%d", &C);
    
    CND[0] = DP[0];
    DP[0] = 0;

    for(int j = 1; j <= K; j++) {
      CND[j] = (CND[j - 1] + DP[j]) % MOD;
    }
    for(int j = 0; j <= K; j++) {
      if(j - C < 0) {
        DP[j] = CND[j] % MOD;
      }
      else {
        DP[j] = (CND[j] - CND[j - C - 1]) % MOD;
      }
    }
  }
  if(DP[K] < 0) DP[K] += MOD;
  printf("%lld\n", DP[K]);
}