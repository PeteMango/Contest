#include <bits/stdc++.h>
using namespace std;

const int MM = 1e5 + 5, INF = 0x3f3f3f3f;
int N, minDiff = INF, psa[MM];

int main () {
  cin >> N;
  psa[0] = 0;
  for(int i = 1; i <= N; i++) {
    cin >> psa[i];
    psa[i] += psa[i-1];
  }
  for(int i = 1; i <= N; i++) {
    minDiff = min(minDiff, abs(psa[N] - 2*psa[i]));
  }
  cout << minDiff << "\n";
}