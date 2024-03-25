#include <bits/stdc++.h>
using namespace std;
const int MAXN = 200005 + 5;

typedef long long ll;
typedef pair<int, int> p;
typedef pair<p, p> PairP;

#define f first
#define s second
#define pb push_back

int N, Q;
p arr[MAXN];
ll bit[MAXN], bitTotal[MAXN], ans[MAXN];
PairP qrys[MAXN];

void update (int val, int pos, ll bit[]){
  for(int i = pos; i <= N; i += i&-i){
    bit[i] += val;
  }
}

ll query (int pos, ll bit[]) {
  ll ret = 0;
  for(int i = pos; i > 0; i -= i&-i) {
    ret += bit[i];
  }
  return ret;
}

ll querySum (int l, int r, ll bit[]){
  return query(r, bit) - query(l - 1, bit);
}

int main(){
  scanf("%d %d", &N, &Q);
  for(int i = 1; i <= N; i++){
    scanf("%d", &arr[i].f);
    arr[i].s = i;
    update(arr[i].f, arr[i].s, bitTotal);
  }
  sort(arr + 1, arr + N + 1);
  for(int i = 1; i <= Q; i++){
    scanf("%d %d %d", &qrys[i].s.f, &qrys[i].s.s, &qrys[i].f.f);
    qrys[i].f.s = i;
  }
  sort(qrys + 1, qrys + Q + 1);
  int idx = 1;
  for(int i = 1; i <= Q; i++){
    while(idx <= N && arr[idx].f < qrys[i].f.f){
      update(arr[idx].f, arr[idx].s, bit);
      idx++;
    }
    ans[qrys[i].f.s] = querySum(qrys[i].s.f, qrys[i].s.s, bitTotal) - 2 * querySum(qrys[i].s.f, qrys[i].s.s, bit);
  }
  for(int i = 1; i <= Q; i++){
    printf("%lld\n", ans[i]);
  }
}