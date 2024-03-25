#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int MAXN = 1e4 + 5, MAXD = 1e2 + 5, MOD = 1e9 + 7;
vector<int> digits;
string s;
int N, D;
LL dp[MAXN][2][MAXD];

LL solve (int pos, int f, int r) {
  if(pos == N) return (r == 0);
  if(dp[pos][f][r] != -1) {
    return dp[pos][f][r];
  }
  LL ans = 0;
  int lmt = (f) ? (digits[pos]) : (9);
  for(int i = 0; i <= lmt; i++) {
    ans += solve(pos+1, f && (i == lmt), (r + i) % D);
  }
  return dp[pos][f][r] = ans % MOD;
}

int main() {
  cin >> s >> D;
  N = (int) s.size();
  for(int i = 0; i < N; i++) {
    digits.push_back(s[i] - '0');
  }
  memset(dp, -1, sizeof(dp));
  LL output = solve(0, 1, 0) - 1;
  if(output < 0) {
    output += MOD;
  }
  printf("%lld\n", output);
}