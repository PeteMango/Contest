#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAXN = 1e5 + 5;
int N;
ll C[MAXN], V[MAXN], ANS;

int main() {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) scanf("%lld %lld", &C[i], &V[i]);
  for(int i = 1; i <= N; i++) {
    if(V[i] > 0) ANS += C[i];
  }
  printf("%lld\n", ANS);
}