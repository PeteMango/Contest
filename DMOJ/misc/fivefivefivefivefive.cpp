#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> p;
#define f first
#define s second

const int MOD = 1e9 + 7, MM = 5e5 + 5;
vector<p> v;
int N;
LL ans=0, suf[MM];

bool sortSecond (pair<LL,LL> a, pair<LL,LL> b) {
  return (a.s > b.s);
}

int main () {
  cin >> N;
  for(int i = 1, first, second; i <= N; i++) {
    cin >> first >> second;
    v.push_back(make_pair(first, second));
  }
  sort(v.begin(), v.end(), sortSecond);
  for(int i = 0; i < N; i++) {
    ans += v[i].f;
  }
  for(int i = 1; i <= N; i++) {
    suf[i] = v[i-1].s;
  }
  for(int i = N-1; i > 0; i--) {
    suf[i] += suf[i+1];
  }
  for(int i = 3; i <= N; i++) {
    ans -= suf[i];
    ans %= MOD;
    if(ans < 0) {
      ans += MOD;
    }
  }
  cout << ans << "\n";
} 