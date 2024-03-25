#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int MM = 1e5 + 5, MOD = 1e9 + 7;
vector<int> vec[MM];
LL dP[MM][2];
int N;

LL solve (int v, int c, int p) {
  if(dP[v][c] != -1) {
    return dP[v][c];
  }
  LL ans=1;
  for(int u:vec[v]) {
    if(u == p) {
      continue;
    }
    if(c == 0) {
      ans = (ans * (solve(u, 0, v) + solve(u, 1, v)))%MOD;
    }
    else {
      ans = (ans * solve(u, 0, v)) % MOD;
    }
  }
  dP[v][c] = ans;
  return dP[v][c];
}

int main() {
  memset(dP, -1, sizeof(dP));
  cin >> N;
  for(int i = 1, u, v; i < N; i++) {
    cin >> u >> v;
    vec[u].push_back(v);
    vec[v].push_back(u);
  }
  printf("%lld\n", ((solve(1, 0, -1) + solve(1, 1, -1))%MOD));
}