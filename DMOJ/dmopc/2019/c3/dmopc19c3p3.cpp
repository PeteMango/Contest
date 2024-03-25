#include <bits/stdc++.h>
using namespace std;
const int MM = 150005;
typedef long long ll;
int N;
ll psa[MM], bit[2 * MM];

/* Inversion: i < j and arr[i] > arr[j] */

void update (int idx){
  for(int i = idx; i < 2 * MM; i += i&-i){
    bit[i]++;
  }
}

ll query (int idx){
  ll ret = 0;
  for(int i = idx; i > 0; i -= i&-i){
    ret += bit[i];
  }
  return ret;
}

int main() {
  scanf("%d", &N);
  for(int i = 1, x; i <= N; i++){
    scanf("%d", &x);
    psa[i] += psa[i - 1];
    if(x == 1) psa[i]++;
    else psa[i]--;
  }
  ll ans = 0;
  update(N + 1);
  for(int i = 1; i <= N; i++){
    update(psa[i] + N + 1);
    ans += query(psa[i] + N);
  }
  printf("%lld\n", ans);
}