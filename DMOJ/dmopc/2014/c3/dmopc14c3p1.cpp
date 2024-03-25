#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int K, D;
ll N;

int main() {
  scanf("%lld %d %d", &N, &K, &D);
  printf("%lld", (ll)(N*pow(K, D)));
}