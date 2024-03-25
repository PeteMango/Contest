#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2005;

int T, N, M, G, cnt = 0, dist[MAXN], foodBasics[MAXN];
vector<pair<int, int>> v[MAXN];

#define pb push_back
#define p push
#define f first
#define s second

void dijkstra (int start) {
  memset(dist, 0x3f, sizeof(dist));
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
  scanf("%d %d %d %d", &T, &N, &M, &G);
  for(int i = 0; i < G; i++) {
    scanf("%d", &foodBasics[i]);
  }
  for(int i = 0, x, y, l; i < M; i++) {
    scanf("%d %d %d", &x, &y, &l);
    v[x].pb(make_pair(y, l));
  }
  dijkstra(0);
  for(int i = 0; i < G; i++){
    if(dist[foodBasics[i]] < T){
      cnt++;
    }
  }
  printf("%d\n", cnt);
}