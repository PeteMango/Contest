#include <bits/stdc++.h>
using namespace std;
int M, N, K, D[1003][30003], mx, cnt;

void update (int x, int y, int R, int v) {
  D[x][y] += v;
  D[x + R][y] -= v;
  D[x][y + R] -= v;
  D[x + R][y + R] += v;
}

int main() {
  scanf("%d %d %d", &M, &N, &K);
  for(int i = 1, x, y, R, B; i <= K; i++){
    scanf("%d %d %d %d", &x, &y, &R, &B);
    for(int j = max(1, x - R); j <= min(N, x + R); j++){
      int dy = sqrt(R * R - (x - j) * (x - j));
      D[j][max(1, y - dy)] += B;
      D[j][min(M + 1, y + dy + 1)] -= B;
    }
  }
  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= M; j++){
      D[i][j] += D[i][j - 1];
      if(D[i][j] >= mx){
        if(D[i][j] == mx) cnt++;
        else {
          mx = D[i][j];
          cnt = 1;
        }
      }
    }
  }
  cout << mx << "\n" << cnt << "\n";
}