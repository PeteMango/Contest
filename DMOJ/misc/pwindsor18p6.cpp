#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAXN = 1e6, INF = 0x3f3f3f3f;

ll N, M, A, B, dist[MAXN], TOT = 0;
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
  cin >> N >> M >> A >> B;
  for(int i = 0, x, y; i < M; i++) {
    scanf("%d %d", &x, &y);
    v[x].pb(make_pair(y, 1));
    v[y].pb(make_pair(x, 1));
  }
  dijkstra(1);
  TOT += dist[A];
  dijkstra(A);
  TOT += dist[B];
  if(TOT > INF) cout << -1 << endl;
  else cout << TOT << endl;
  
}