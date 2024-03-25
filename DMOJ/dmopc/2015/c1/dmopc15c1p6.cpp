#include <bits/stdc++.h>
using namespace std;
const int SIZE = (2e5 + 5);
typedef long long ll;
int N, M, Q;
struct node {int l, r; ll  lz, sum;} seg[3*SIZE];

/* Modular Formulas
(a+b)%p = (a%p+b%p)%p
(a*b)%p = (a%p*b%p)%p
(a/b)%p = (a*b^-1)%p
*/

void push_up(int idx){
  seg[idx].sum = seg[2*idx].sum + seg[2*idx+1].sum;
}

void push_down(int idx){
  seg[2 * idx].lz += seg[idx].lz;
  seg[2*idx+1].lz += seg[idx].lz;
  seg[2*idx].sum += seg[idx].lz * (seg[2*idx].r-seg[2*idx].l+1);
  seg[2*idx+1].sum += seg[idx].lz * (seg[2*idx+1].r-seg[2*idx+1].l+1);
  seg[idx].lz = 0;
}

void build(int l, int r, int idx){
  seg[idx].l = l;
  seg[idx].r = r;
  if(l == r){
    cin >> seg[idx].sum;
    return;
  }
  int mid = (seg[idx].l + seg[idx].r)/2;
  build(l, mid, 2*idx); 
  build(mid + 1, r, 2*idx+1);
  push_up(idx);
}

void update(int l, int r, int val, int idx){
    if(seg[idx].l == l &&seg[idx].r == r){
    seg[idx].lz += val;
    seg[idx].sum += (ll) val * (r-l+1);
    return;
  }
  if(seg[idx].lz != 0){
    push_down(idx);
  }
  int mid = (seg[idx].l+seg[idx].r)/2;
  if(r <= mid) update(l, r, val, 2*idx);
  else if(l > mid) update (l, r, val, 2*idx+1);
  else {
    update(l, mid, val, 2 * idx);
    update(mid+1, r, val, 2 * idx + 1);
  }
  push_up(idx);
}

ll querySum(int l, int r, int idx){
  if(seg[idx].l == l && seg[idx].r == r) return seg[idx].sum;
  if(seg[idx].lz != 0) push_down(idx);
  int mid = (seg[idx].l + seg[idx].r)/2;
  if(r <= mid) return querySum(l, r, 2*idx);
  else if(l > mid) return querySum(l, r, 2*idx+1);
  else{
    return querySum(l, mid, 2 * idx) + querySum(mid+1, r, 2 * idx + 1);
  }
}

int main() {
  scanf("%d %d %d", &M, &N, &Q);
  build(1, N, 1);
  for(int i = 1, op, x, y, z; i <= Q; i++){
    scanf("%d %d %d", &op, &x, &y);
    if(op == 1){
      scanf("%d", &z);
      update(x, y, z, 1);
    }
    else {
      cout << (querySum(x, y, 1) % M) << endl;
    }
  }
}