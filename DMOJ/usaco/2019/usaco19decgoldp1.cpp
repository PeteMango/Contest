#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef pair<int, pii> edge; 
typedef pair<int, pii> vertex; 

#define pb push_back
#define f first
#define s second

const int MM = 1005;
int N, M, dp[MM][MM];
vector<edge> edges[MM];

int main() {
  memset(dp, 1, sizeof(dp));
  scanf("%d%d", &N, &M);
  dp[1][1000] = 0;
  for(int i = 1, a, b, c, f; i <= M; i++) {
    scanf("%d%d%d%d", &a, &b, &c, &f);
    edges[a].pb(edge(b, {f, c}));
    edges[b].pb(edge(a, {f, c}));
  }
  priority_queue<vertex> q;
  q.push(vertex(0, {1, 1000}));
  double ret = -1;
  while(q.size()) {
    vertex curr = q.top(); q.pop();
    if(curr.s.f == N) {
      ret = max(ret, curr.s.s / (double)dp[curr.s.f][curr.s.s]);
      continue;
    }
    for(edge out: edges[curr.s.f]) {
      int nf = min(out.s.f, curr.s.s);
      int nc = dp[curr.s.f][curr.s.s] + out.s.s;
      int nd = out.f;
      if(nc < dp[nd][nf]) {
        dp[nd][nf] = nc;
        q.push(vertex(-dp[nd][nf], {nd, nf}));
      }
    }
  }
  printf("%d\n", (int)(1000000 * ret));
}