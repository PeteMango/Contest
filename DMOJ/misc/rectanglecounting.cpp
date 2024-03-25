#include <bits/stdc++.h>
using namespace std;

#define pb push_back

const int MM = 1e6+5;
typedef long long LL;
struct E { int x, lo, hi, v; }; //+1 for left edge, -1 for right edge

int N, bt[MM], tp[MM];
LL ans;
vector<E> event;

bool cmp (E a, E b) {
  return a.x < b.x || (a.x == b.x && a.v < b.v);
}

void upd (int bit[], int pos, int val) {
  for(int i = pos; i < MM; i += i&-i) {
    bit[i] += val;
  }
}

int qry (int bit[], int pos) {
  int ret=0;
  for(int i = pos; i > 0; i -= i&-i) {
    ret += bit[i];
  }
  return ret;
}

int main() {
  cin >> N;
  for(int i = 1, a, b, c, d; i <= N; i++) {
    cin >> a >> b >> c >> d;
    event.pb({a, b, d, 1});
    event.pb({c, b, d, -1});
  }
  sort(event.begin(), event.end(), cmp);
  for(E e:event) {
    if(e.v < 0) {
      ans += qry(bt, e.hi-1)-qry(tp, e.lo)-1;
      upd(bt, e.lo, -1); upd(tp, e.hi, -1);
    }
    else {
      upd(bt, e.lo, 1);
      upd(tp, e.hi, 1);
    }
  }
  cout << ans << "\n";
}