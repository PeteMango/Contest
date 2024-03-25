#include <bits/stdc++.h>
using namespace std;
const int MM = 1e5 + 2;
int N, W, dp[MM], mx = 1e5;

int main () {
  cin >> N >> W;
  memset(dp, 0x3f, sizeof(dp));
  dp[0] = 0;
  for(int i = 1, w, v; i <= N; i++) {
    cin >> w >> v;
    for(int j = mx; j >= v; j--) {
      dp[j] = min(dp[j], dp[j - v] + w);
    }
  }
  for(int i = mx; i >= 0; i--) {
    if(dp[i] <= W) {
      cout << i << endl;
      return 0;
    }
  }
}