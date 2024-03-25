#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL;
#define INF 2000000000
#define F first
#define S second

int N, M;
vector<pair<LL,LL>> intervaL;
 
bool check (LL d) {
  LL prev = -1LL*INF*INF;
  int cnt = 0;
  for (auto& i : intervaL) {
    while (max(prev + d, i.F) <= i.S) {
      prev = max(prev + d, i.F);
      cnt++;
      if (cnt >= N) { 
        break;
      }
    }
    if (cnt >= N) {
      break;
    }
  }
  return (cnt >= N);
}
 
int main() {
  scanf("%d%d", &N, &M);
  intervaL.resize(M);
  for (int i = 0; i < M; i++) {
    cin >> intervaL[i].F >> intervaL[i].S;
  }
  sort(intervaL.begin(), intervaL.end());
  LL L = 1, H = 1LL*INF*INF, res = -1;
  while (L <= H) {
    LL M = (L+H)/2;
    if (check(M)) {
      res = M;
      L = M + 1;
    }
    else {
      H = M - 1;
    }
  }
  printf("%lld\n", res);
}