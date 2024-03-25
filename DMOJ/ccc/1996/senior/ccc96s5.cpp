#include <bits/stdc++.h>
using namespace std;

#define pb push_back

int N, L, mx = 0;
vector<int> a, b;
int main() {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) {
    scanf("%d", &L);
    for(int j = 1, T; j <= L; j++) {
      scanf("%d", &T);
      a.pb(T);
    }
    for(int j = 1, T; j <= L; j++) {
      scanf("%d", &T);
      b.pb(T);
    }
    for(int i = 0; i < L-1; i++) {
      for(int j = i+1; j < L; j++) {
        if(b[j] >= a[i] && j-i > mx) {
          mx = j-i;
        }
      }
    }
    printf("The maximum distance is %d\n", mx);
    a.clear(); b.clear(); mx = 0;
  }
}