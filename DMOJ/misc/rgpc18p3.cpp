#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MM = 1000005;
ll N, T, L, Lft = 1, Rgt = 1, S, MX, A[MM];

int main () {
  scanf("%lld %lld", &N, &T);
  for(int i = 1, a, b, c; i <= T; i++) {
    scanf("%d %d %d", &a, &b, &c);
    A[a] += c;
    A[b + 1] -= c;
  } 
  for(int i = 1; i <= N; i++) {
    A[i] += A[i - 1];
  }
  scanf("%lld", &L);
  while(Lft <= N) {
    bool F = false;
    while(Rgt <= N - 1) {
      if(S + A[Rgt + 1] <= L) {
        S += A[Rgt + 1];
        F = true;
        Rgt++;
      }
      else {
        break;
      }
    }
    if(F) {
      MX = max(MX, Rgt - Lft + 1);
      S -= A[Lft];
    }
    Lft++;
  }
  printf("%lld\n", MX);
}