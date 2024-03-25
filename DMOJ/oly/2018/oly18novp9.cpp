#include <bits/stdc++.h>
using namespace std;
const int MM = 12;
int N, L, R, d[MM], dp[MM][10][2];

int func (int pos, int prev, int lmt) {
  if(pos < 0) {
    return 1;
  }
  if(dp[pos][prev][lmt] != 0) {
    return dp[pos][prev][lmt];
  }
  int up = lmt ? d[pos] : 9, ret = 0;
  for(int i = 0; i <= up; i++) {
    if(abs(i - prev) >= 2) {
      ret += func(pos-1, i, lmt&&i == d[pos]);
    }
  }
  return dp[pos][prev][lmt] = ret;
}

int solve (int x) {
  N = 0;
  for(; x; x /= 10) {
    d[N++] = x % 10;
  }
  int cnt = 0;
  for(int i = 0; i < N; i++) {
    int up = (i == N-1) ? d[N-1]:9;
    for(int j = 1; j <= up; j++) {
      cnt += func(i-1, j, i == N-1 && j == d[N-1]);
    }
  }
  return cnt;
}

int main() {
  scanf("%d%d", &L, &R);
  if(L > R) swap(L, R);
  printf("%d\n", solve(R)-solve(L-1));
}