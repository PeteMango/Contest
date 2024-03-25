#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define LL long long

const int MM = 1e5 + 5;
int N, M;
LL ans=0;
pair<int, int> a[MM];

int main () {
  cin >> N >> M;
  for(int i = 1; i <= N; i++) {
    cin >> a[i].f >> a[i].s;
  }
  sort(a+1, a+N+1);
  for(int i = 2; i <= N+1; i++) {
    if(a[i-1].s > a[i].s) {
      ans += a[i-1].s - a[i].s;
    }
  }
  cout << ans << "\n";
}
