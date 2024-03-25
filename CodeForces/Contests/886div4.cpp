#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;
const int MM = 2e5 + 5;
vector<pair<int, int> >adj[MM];
bool vis[MM];
int coord[MM];

void dfs (int u) {
    vis[u] = true;
    for(auto x : adj[u]) {
        int v = x.first, w = x.second;
        if(!vis[v]) {
            coord[v] = coord[u] + w;
            dfs(v);
        }
    }
}

void solve () {
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; i++) {
        adj[i].clear();
        coord[i] = 0;
        vis[i] = false;
    }
    vector<array<int, 3>> q;
    for(int i = 1, a, b, d; i <= m; i++) {
        cin >> a >> b >> d;
        adj[a].push_back(make_pair(b, d));
        adj[b].push_back(make_pair(a, -d));
        q.push_back({a, b, d});
    }
    for(int i = 1; i <= n; i++) {
        if(!vis[i]) {
            dfs(i);
        }
    }
    for(int i = 0; i < m; i++) {
        int a = q[i][0], b = q[i][1], d = q[i][2];
        if(coord[a] + d != coord[b]) {
            printf("NO\n");
            return;
        }
    }
    printf("YES\n");
}

int main () {
    cin >> T;
    while(T--) {
        solve();
    }
}