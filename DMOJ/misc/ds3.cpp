#include <iostream>
#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;
const int MM = 1e5 + 5;
struct node {int l, r, v, g, f;} seg[3 * MM];
int N, M;
char op;

void push_up(int idx){
  seg[idx].v = min(seg[2 * idx].v, seg[2 * idx + 1].v);
  seg[idx].g = __gcd(seg[2 * idx].g , seg[2 * idx + 1].g);
  seg[idx].f = 0;
  if(seg[idx].g == seg[2 * idx].g) seg[idx].f += seg[2 * idx].f;
  if(seg[idx].g == seg[2 * idx + 1].g) seg[idx].f += seg[2 * idx + 1].f;
}

void build(int l, int r, int idx){
  seg[idx].l = l;
  seg[idx].r = r;
  if(l == r) {
    scanf("%d", &seg[idx].v); 
    seg[idx].g = seg[idx].v; 
    seg[idx].f = 1;
    return;}
  int mid = (seg[idx].l + seg[idx].r) / 2;
  build(l, mid, 2 * idx);
  build(mid + 1, r, 2 * idx + 1);
  push_up(idx);
}

void update(int pos, int val, int idx){
  if(seg[idx].l == pos && seg[idx].r == pos){
    seg[idx].v = seg[idx].g = val;
    return;
  }
  int mid = (seg[idx].l + seg[idx].r) / 2;
  if(pos <= mid) update(pos, val, 2 * idx);
  else update(pos, val, 2 * idx + 1);
  push_up(idx);
}

int qryMin(int l, int r, int idx){
  if(seg[idx].l == l && seg[idx].r == r){
    return seg[idx].v;
  }
  int mid = (seg[idx].l + seg[idx].r) / 2;
  if(r <= mid) return qryMin(l, r, 2 * idx);
  else if(l > mid) return qryMin(l, r, 2 * idx + 1);
  else return min(qryMin(l, mid, 2 * idx), qryMin(mid + 1, r, 2 * idx + 1));
}

int qryGcd(int l, int r, int idx){
  if(seg[idx].l == l && seg[idx].r == r){
    return seg[idx].g;
  }
  int mid = (seg[idx].l + seg[idx].r) / 2;
  if(r <= mid) return qryGcd(l, r, 2 * idx);
  else if(l > mid) return qryGcd(l, r, 2 * idx + 1);
  else return __gcd(qryGcd(l, mid, 2 * idx), qryGcd(mid + 1, r, 2 * idx + 1));
}

int qryCnt(int l, int r, int g, int idx){
  if(seg[idx].l == l && seg[idx].r == r){
    return g== seg[idx].g? seg[idx].f:0;
  }
  int mid = (seg[idx].l + seg[idx].r) / 2;
  if(r <= mid) return qryCnt(l, r, g, 2 * idx);
  if(l > mid) return qryCnt(l, r, g, 2 * idx + 1);
  return qryCnt(l, mid, g, 2 * idx) + qryCnt(mid + 1, r, g, 2 * idx + 1);
}

int main() {
  scanf("%d %d", &N, &M);
  build(1, N, 1);
  for(int i = 1, x, y; i <= M; i++){
    scanf(" %c %d %d", &op, &x, &y);
    if(op == 'C') update(x, y, 1);
    else if(op == 'M') printf("%d\n", qryMin(x, y, 1));
    else if(op == 'G') printf("%d\n", qryGcd(x, y, 1));
    else if(op == 'Q'){
      int g = qryGcd(x, y, 1);
      printf("%d\n", qryCnt(x, y, g, 1));
    }
  }
  return 0;
}