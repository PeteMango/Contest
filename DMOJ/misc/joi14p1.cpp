#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define f first
#define s second
typedef long long LL;
typedef pair<int, int> pi;

const int MM = 5e5 + 5, LOG = 20;
const LL INF = 0x3f3f3f3f3f3f3f3f;
int N, sz[MM], lvl[MM], pa[MM];
LL dis[LOG][MM], tmp[MM], ans;
bool done[MM];
vector<pi> adj[MM];

void getsz (int u, int pre) {
  sz[u] = 1;
  for(pi e : adj[u]) {
    if(e.f != pre && !done[e.f]) {
      getsz(e.f, u);
      sz[u] += sz[e.f];
    }
  }
}

int getcent (int u, int pre, int tot) {
  for(pi e : adj[u]) {
    if(e.f != pre && !done[e.f] && 2*sz[e.f] > tot) {
      return getcent(e.f, u, tot);
    }
  }
  return u;
}

void dfs (int u, int pre, int level, LL d) {
  dis[level][u] = d;
  for(pi e : adj[u]) {
    if(e.f != pre && !done[e.f]) {
      dfs(e.f, u, level, d+e.s);
    }
  }
}

void solve (int rt, int pre, int level) {
  getsz(rt, -1);
  rt = getcent(rt, -1, sz[rt]);
  done[rt] = true;
  lvl[rt] = level;
  pa[rt] = pre;
  dfs(rt, -1, level, 0);
  for(pi e : adj[rt]) {
    if(!done[e.f]) {
      solve(e.f, rt, level+1);
    }
  }
}

void Init(int n, int A[], int B[], int D[]) {
  N = n;
  memset(tmp, 0x3f, sizeof(tmp));
  for(int i = 0; i < N-1; i++) {
    adj[A[i]].pb({B[i], D[i]});
    adj[B[i]].pb({A[i], D[i]});
  }
  solve(1, -1, 0);
}

LL Query(int S, int X[], int T, int Y[]) {
  ans = INF;
  for(int i = 0; i < S; i++) {
    for(int v = X[i], u = X[i], cnt = lvl[X[i]]; u != -1; u = pa[u], cnt--) {
      tmp[u] = min(tmp[u], dis[cnt][v]);
    }
  }
  for(int i = 0; i < T; i++) {
    for(int v = Y[i], u = Y[i], cnt = lvl[Y[i]]; u != -1; u = pa[u], cnt--) {
      ans = min (ans, tmp[u] + dis[cnt][v]);
    }
  }
  for(int i = 0; i < S; i++) {
    for(int v = X[i], u = X[i], cnt = lvl[X[i]]; u != -1; u = pa[u], cnt--) {
      tmp[u] = INF;
    }
  }
  return ans;
}

int main () {
  int n, m, a[100], b[100], d[100], x[100], y[100];
  cin >> n;
  for(int i = 0; i < n-1; i++) {
    cin >> a[i] >> b[i] >> d[i];
  }
  Init(n, a, b, d);
  for(int i = 0, s, t; i < m; i++) {
    cin >> s >> t;
    for(int j = 0; j < s; j++) {
      cin >> x[j];
    }
    for(int j = 0; j < t; j++) {
      cin >> y[j];
    }
    cout << Query(s, x, t, y) << endl;
  }
}

  