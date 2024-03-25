#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define f first
#define s second
typedef pair<int,int> pii;
int L, N;
vector<pii> v;

int main () {
  cin >> L >> N;
  for(int i = 1, x, y; i <= N; i++) {
    cin >> x >> y;
    v.pb(make_pair(x, y));
  }
  sort(v.begin(), v.end());
  int ans = v[0].f, Lft = v[0].f, Rgt = v[0].s;
  for(int i = 1; i < v.size(); i++) {
    if(v[i].f > Rgt) {
      ans = max(ans, v[i].f - Rgt);
      Lft = v[i].f;
    }
    Rgt =max(Rgt ,v[i].s);
  }
  ans = max(ans, L - Rgt);
  cout << ans << "\n";
}