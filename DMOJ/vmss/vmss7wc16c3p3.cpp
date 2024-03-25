#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2005, INF = 0x3f3f3f3f;

int N, M, B, Q, dist[MAXN];
vector<pair<int, int>> v[MAXN];

#define pb push_back
#define p push
#define f first
#define s second

void dijkstra (int start) {
  for(int i = 0; i < MAXN; i++) dist[i] = INF;
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
  scanf("%d %d %d %d", &N, &M, &B, &Q);
  for(int i = 0, x, y, l; i < M; i++) {
    scanf("%d %d %d", &x, &y, &l);
    v[x].pb(make_pair(y, l));
    v[y].pb(make_pair(x, l));
  }
  dijkstra(B);
  for(int i = 0, h; i < Q; i++){
    scanf("%d", &h);
    if(dist[h] == INF) printf("%d\n", -1);
    else printf("%d\n", dist[h]);
  }
}