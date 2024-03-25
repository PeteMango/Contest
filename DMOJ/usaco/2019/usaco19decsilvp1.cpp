#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
ll N, M, R[] = {1, 2, 4, 7, 8, 11, 13, 14};

int main () {
  scanf("%d", &N);
  M = (N - 1) / 8;
  printf("%lld\n", R[N-8*M-1]+15*M);
}
 
