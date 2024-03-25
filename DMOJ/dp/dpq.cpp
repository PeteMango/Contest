#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAXN = 2e5 + 5;
int N;
ll ANS, H[MAXN], A[MAXN], BIT[MAXN], DP[MAXN];

void upd (int idx, ll val) {
  for(int i = idx; i <= N; i += i&-i) {
    BIT[i] = max(BIT[i], val);
  }
}

ll qry (int idx) {
  ll ret = 0;
  for(int i = idx; i > 0; i -= i & -i) {
    ret = max(ret, BIT[i]);
  }
  return ret;
}

int main () {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) {
    scanf("%lld", &H[i]);
  }
  for(int i = 1; i <= N; i++) {
    scanf("%lld", &A[i]);
  }
  for(int i = 1; i <= N; i++) {
    DP[i] = qry(H[i] - 1) + A[i];
    upd(H[i], DP[i]);
  }
  for(int i = 1; i <= N; i++) {
    ANS = max(ANS, DP[i]);
  }
  printf("%lld\n", ANS);
}