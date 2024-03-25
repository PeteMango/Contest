#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 5, INF = 0x3f3f3f3f;

int N, M, maxANS = 0, home[MAXN], washington[MAXN];
vector<pair<int, int>> v[MAXN];

#define pb push_back
#define p push
#define f first
#define s second

void dijkstra (int start, int dist[]) {
  for(int i = 0; i < N; i++) dist[i] = INF;
  queue<int> q;
  q.p(start);
  dist[start] = 0;
  while(!q.empty()) {
    int cur = q.front();
    for(pair<int, int> e:v[cur]){
      int connected = e.f, curDist = dist[cur] + e.s;
      if(curDist < dist[connected]) {
        q.p(connected);
        dist[connected] = curDist;
      }
    }
    q.pop();
  }
}

int main () {
  scanf("%d %d", &N, &M);
  for(int i = 0, x, y, l; i < M; i++) {
    scanf("%d %d %d", &x, &y, &l);
    v[x].pb(make_pair(y, l));
    v[y].pb(make_pair(x, l));
  }
  dijkstra(0, home);
  dijkstra(N - 1, washington);
  for(int i = 0; i < N; i++) {
    if(home[i] + washington[i] > maxANS) {
      maxANS = home[i] + washington[i];
    }
  }
  printf("%d\n", maxANS);
}
