#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7, NN = 2e3 + 5;
int N, S, T, ans, f[NN][NN];

void up (int &x, int y) {
  x += y;
  if(x >= MOD) {
    x -= MOD;
  }
}

int solve (int s, int t) {  
  memset(f, 0, sizeof(f));
  f[0][0] = 1;
  for(int i = 0, k; i < N-1; i++) {
    for(int j = 0; j <= i; j++) {
      if(f[i][j]) {
        if(i + 1 == s) {
          up(f[i + 1][j + 1], f[i][j]);
        }
        else if(i + 1 == t) {
          if(N & 1) {
            up(f[i + 1][j + 1], f[i][j]);
          }
          else {
            up(f[i + 1][j], 1ll * f[i][j] * (j - (s <= i)) % MOD);
          }
        }
        else {
          k = (s <= i) + (t <= i);
          up(f[i + 1][j + 1], f[i][j]);
          up(f[i + 1][j - 1], 1ll * (j - k) * (j - 1) % MOD * f[i][j] % MOD);
        } 
      }
    }
  }
  return f[N - 1][2 - (s == N || t == N)];
}

int main () {
  scanf("%d %d %d", &N, &S, &T);
  if(N == 1) {
    printf("1\n");
    return 0;
  }
  if(S == T) {
    printf("0\n");
    return 0;
  }
  ans = solve(S, T);
  ans = (ans + solve(N-S+1, N-T+1)) % MOD;
  if(ans < 0) {
    ans += MOD;
  }
  printf("%d\n", ans);
}