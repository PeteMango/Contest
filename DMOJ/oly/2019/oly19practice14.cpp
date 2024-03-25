#include <bits/stdc++.h>
using namespace std;
#define f(a, b) for(int i = a; i <= b; i++)
#define F(a, b) for(int i = a; i >= b; i--)
#define print(i) printf("%lld\n", i);
const int  MM = 1e6 + 5;
int N, arr[MM], mA[MM], mI[MM];
long long suM;

int main() {
  scanf("%d", &N);
  f(1, N) {
    scanf("%d", &arr[i]);
    if(i > 1) {
      mA[i] = mA[i-1];
    }
    mA[i] = max(mA[i], arr[i]);
  }
  F(N, 1) {
    if(i < N) {
      mI[i] = mI[i+1];
    }
    mI[i] = max(mI[i], arr[i]);
  }
  f(1, N) {
    suM += max(0, min(mA[i], mI[i])-arr[i]);
  }
  print(suM);
}