#include <bits/stdc++.h>
using namespace std;
#define LL long long
const int MM = 1e5 + 5;
LL N, M, sum=0, f[MM];

int main () {
  cin >> N >> M;
  for(LL i = 1; i <= N; i++) cin >> f[i];
  sort(f+1, f+N+1);
  for(LL i = M+1; i <= N; i++) sum += f[i];
  cout << sum << "\n";
}