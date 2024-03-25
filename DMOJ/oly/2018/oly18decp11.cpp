#include <bits/stdc++.h>
using namespace std;

#define pb push_back
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int,int> pii;
const int MAXN = 20005;

#define weight first
#define nxt second

int N, M, K, Q;
vector<pii> adj[MAXN], adj2[MAXN];
int dis[202][MAXN], dis2[202][MAXN];

void dijkstra (int start, int hub) {
  priority_queue<pii, vector<pii>, greater<pii>> pq;
  pq.push({0, start});
  for(int i=0; i<=N; i++) dis[hub][i] = 0x3f3f3f3f;
  dis[hub][start]=0;
  while(!pq.empty()) {
    pii cur = pq.top(); pq.pop();
    if(cur.weight > dis[hub][cur.nxt]) continue;
    for(pii v : adj[cur.nxt]) {
      if(dis[hub][v.nxt] > cur.weight + v.weight)  {
        dis[hub][v.nxt] = cur.weight + v.weight;
        pq.push({dis[hub][v.nxt], v.nxt});
      }
    }
  }
} 

void dijkstra2(int start, int hub) {
  priority_queue<pii, vector<pii>, greater<pii>> pq;
  pq.push({0, start});
  for(int i=0; i<=N; i++) dis2[hub][i] = 0x3f3f3f3f;
  dis2[hub][start]=0;
  while(!pq.empty()) {
    pii cur = pq.top(); pq.pop();
    if(cur.weight > dis2[hub][cur.nxt]) continue;
    for(pii v : adj2[cur.second]) {
      if(dis2[hub][v.nxt] > cur.weight + v.weight)  {
        dis2[hub][v.nxt] = cur.weight + v.weight;
        pq.push({dis2[hub][v.nxt], v.nxt});
      }
    }
  }
}
 
int main () {
  cin.tie(0);
  cin.sync_with_stdio(0);
  cin >> N >> M >> K >> Q;
  for(int i = 0, u, v, c; i < M; i++) {
    cin >> u >> v >> c;
    adj[u].pb(make_pair(c, v));
    adj2[v].pb(make_pair(c, u));
  }
  for(int i = 1, d; i <= K; i++) {
    cin >> d;
    dijkstra(d, i);
    dijkstra2(d, i);
  }
  int ans=0, cnt=0;
  while(Q--) {
    int u, v; cin >> u >> v;
    int best=0x3f3f3f3f;
    for(int i=1; i<=K; i++) {
      best=min(best, dis2[i][u] + dis[i][v]);
    }
    if(best != 0x3f3f3f3f) ans += best, cnt++;
  }
  cout << cnt << endl;
  cout << ans << endl;
}
