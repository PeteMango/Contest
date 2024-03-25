#include <iostream>
#include <stdio.h>

int N, bit[32003], lvl[32003];
void update(int pos, int val){
  for(int i = pos; i < 32003; i += i&-i){
    bit[i] += val;
  }
}
int query(int pos){
  int ret = 0;
  for(int i = pos; i > 0; i -= i&-i){
    ret += bit[i];
  }
  return ret;
}
int main() {
  scanf("%d", &N);
  for(int i = 1, x, y, val; i <= N; i++){
      scanf("%d %d", &x, &y);
      x++; y++;
      val = query(x);
      lvl[val]++;
      update(x, 1);
  }
  for(int i = 0; i < N; i++){
    printf("%d\n", lvl[i]);
  }
}