#include <bits/stdc++.h>
using namespace std;

const int MM = 1e5 + 5, INF = 0x3f3f3f3f;
int N, M, b, a[MM];

int main() {
  scanf("%d%d", &N, &M);
  for(int i = 1; i <= N; i++) {
    scanf("%d", &a[i]);
    a[i] += a[i-1];
  }
  for(int i = 1, mx = -INF; i <= M; i++) {
    scanf("%d", &b);
    for(int j = b; j <= N; j++) {
      if(a[j]-a[j-b] >= mx) {
        mx = a[j]-a[j-b];
      }
    }
    printf("%d\n", mx);
  }
}
