#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
const int MM = 1e5+5;
int N, sz[MM]; vector<pi> adj[MM]; bool done[MM]; ll ans; char c; unordered_map<int, int> mp;
void getsz(int u, int pre){
    sz[u] = 1;
    for(pi e: adj[u]){
        int v = e.first;
        if(v != pre && !done[v]) { getsz(v, u); sz[u] += sz[v]; }
    }
}
int getCent(int u, int pre, int tot){
    for(pi e: adj[u]){
        int v = e.first;
        if(v != pre && !done[v] && sz[v]*2 > tot) return getCent(v, u, tot);
    }
    return u;
}
void dfs(int u, int pre, int sum, vector<int>& path){
    path.push_back(sum);  ans += mp[1-sum] + mp[-1-sum];  // x + sum = 1 / -1
    for(pi e: adj[u]){
        int v = e.first, w = e.second;
        if(v != pre && !done[v]) dfs(v, u, sum+w, path);
    }
}
void solve(int rt, int pre){
    getsz(rt, pre);  rt = getCent(rt, pre, sz[rt]);
    done[rt]=1;  mp.clear(); mp[0] = 1;
    for(pi e: adj[rt]){
        int v = e.first, w = e.second;
        if(v != pre && !done[v]){
            vector<int> path;  dfs(v, rt, w, path);
            for(int x: path) mp[x]++;
        }
    }
    for(pi e: adj[rt]){
        int v = e.first;
        if(v!= pre && !done[v]) solve(v, rt);
    }
}
int main(){
    scanf("%d", &N);
    for(int i=1, u, v, w; i<N; i++){
       scanf("%d %d %c", &u, &v, &c); w = (c=='r'? -1:1);
       adj[u].push_back({v, w}); adj[v].push_back({u, w});
    }
    solve(1, 0); printf("%lld\n", ans - (N-1));
}