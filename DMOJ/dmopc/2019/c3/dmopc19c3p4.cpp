#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MM = 3e5 + 5;
int N, clr[MM];
string s;
vector<int> adj[MM];
ll dp[MM], ans, mod = 1e9 + 7;

void dfs(int u, int pa, int val) {
  ll v1 = 0, v2 = 0;
  for(int v:adj[u]) {
    if(v == pa) continue;
    dfs(v, u, val);
    v2 += (v1 + v2) * dp[v];
    v1 += dp[v];
    v1 %= mod;
    v2 %= mod;
  }
  if(clr[u] == val){
    dp[u] = (1 + v1 + v2) % mod;
    ans = (ans + dp[u]) % mod;
  }
  else {
    dp[u] = (v1 + v2) % mod;
    ans = (ans + v2) % mod;
  }
}

int main() {
  cin >> N >> s;
  for(int i = 1; i <= N; i++) clr[i] = s[i - 1] == 'R';
  for(int i = 1, u, v; i < N; i++){
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  dfs(1, 0, 1); dfs(1, 0, 0);
  cout << ans << endl;
}