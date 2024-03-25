#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAXN = 3005;
int N;
ll DP[MAXN][MAXN], A[MAXN];

int main() {
  scanf("%d", &N);
  for(int i = 0; i < N; i++) {
    scanf("%lld", &A[i]);
  }
  for(int i = N - 1; i >= 0; i--) {
    for(int j = i + 1; j <= N; j++) {
      DP[i][j] = max(A[i] - DP[i + 1][j], A[j - 1] - DP[i][j - 1]);
    }
  }
  printf("%lld\n", DP[0][N]);
}