#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
int N, minX = INF, minY = INF, maxX = -INF, maxY = -INF; 
char op;
int main(){
  scanf("%d", &N);
  for(int i = 1, x, y; i <= N; i++) {
    cin >> x >> op >> y;
    minX = min(minX, x); maxX = max(maxX, x);
    minY = min(minY, y); maxY = max(maxY, y);
  }
  printf("%d,%d\n%d,%d", (minX-1), (minY-1), (maxX+1), (maxY+1));
}