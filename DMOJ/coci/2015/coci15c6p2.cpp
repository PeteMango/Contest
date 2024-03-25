#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
int N, C, mx = 0, f[MAXN];

int main () {   
  scanf("%d %d", &N, &C);
  for(int i = 1; i <= N; i++) {
    scanf("%d", &f[i]);
  }
  for(int i = 1; i <= N; i++) {
    int crnt = 0, ans = 0;
    for(int j = i; j <= N; j++) { 
        if(crnt + f[j] <= C) {
            crnt += f[j];
            ans++;
        }
    }
    mx = max(ans, mx);
  }
  printf("%d\n", mx);
}