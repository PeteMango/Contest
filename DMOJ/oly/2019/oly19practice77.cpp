#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> PI;
typedef long long LL;

#define pb push_back

const int MM = 1e5 + 5;
int N;
LL L, pas, no_pas;
vector<int> st, ed;

int main () {
  cin >> N >> L;
  for(int i = 1, x, y; i <= N; i++) {
    cin >> x >> y;
    pas += abs(y - x);
    st.pb(x);
    ed.pb(y);
  }
  st.pb(L); ed.pb(0);
  sort(st.begin(), st.end());
  sort(ed.begin(), ed.end());
  for(int i = 0; i < st.size(); i++) {
    no_pas += abs(st[i] - ed[i]);
  }
  cout << pas + no_pas << "\n";
}