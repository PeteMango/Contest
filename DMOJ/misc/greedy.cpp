#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define f first
#define s second
ll N, M, CNT = 0, CUR = 0;
vector<pair<ll, ll>> v;
int main() {
  cin >> N >> M;
  for(int i = 0, p, s; i < N; i++) {
    cin >> p >> s;
    v.pb(make_pair(p, s));
  }
  sort(v.begin(), v.end());
  for(int i = 0; i < N; i++){
    if(CUR + v[i].s <= M) {
      CNT += v[i].f * v[i].s;
      CUR += v[i].s;
    }
    else {
      CNT += v[i].f * (M - CUR);
      break;
    }
  }
  cout << CNT << endl;
}