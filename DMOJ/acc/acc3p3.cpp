#include <bits/stdc++.h>
using namespace std;
const int MM = 1e5 + 5, MX = INT_MAX;
vector<int> pos[MM];
int N, M, x[MM], num;
string in[MM];

int main() {
  scanf("%d", &N);
  for(int i = 0; i < N; i++) {
    cin >> in[i];
  }
  for(int i = 25; i >= 0; i--) {
    M = MX;
    for(int j = 0; j < N; j++) {
      pos[j].clear();
      for(int k = x[j]; k < in[j].size(); k++) {
        if(in[j][k] - 'a' == i) {
          pos[j].push_back(k);
        }
      }
    }
    for(int j = 0; j < N; j++) {
      M = min(M, (int) pos[j].size());
    }
    if (M == 0) continue;
    for(int j = 0; j < N; j++) {
      x[j] = max(x[j], pos[j][M-1]);
    }
    for(int j = 0; j < M; j++) {
      cout << (char) ('a' + i);
    }
    num += M;
  }
  if(num == 0) {
    printf("-1");
  }
  printf("\n");
}