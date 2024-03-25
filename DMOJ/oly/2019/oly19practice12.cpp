#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
const int MM = 2e5 + 5;
LL N, K, arr[MM], dP[2][MM], tmp[2][MM], a, b=1;

int main () {
  cin >> N >> K;
  for(int i = 1; i <= N; i++) {
    cin >> arr[i];
    arr[i] += arr[i-1];
  }
  for(int i = 1; i <= K; i++) {
    dP[b][0] = tmp[b][0] = LLONG_MIN/4;
    for(int j = 1; j <= N; j++) {
      tmp[b][j] = max(tmp[b][j-1], dP[a][j-1]-arr[j-1]);
      dP[b][j] = max(dP[b][j-1], tmp[b][j]+arr[j]);
    }
    swap(a, b);
  }
  cout << dP[a][N] << "\n";
}