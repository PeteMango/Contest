#include <bits/stdc++.h>
using namespace std;
int T;
 
vector<vector<int>> tree;
vector<int> cnt;

void reset (int N) {
    tree.clear();
    tree.resize(N+1);

    cnt = vector<int>(N+1, 0);
}

int dfs (int cur, int parent) {
    if(cur != 0 && tree[cur].size() == 1) {
        return cnt[cur] = 1;
    }
    for(auto x : tree[cur]) {
      if(x != parent) {
        cnt[cur] += dfs(x, cur);
      }
    }
    return cnt[cur];
} 

int main () {
    cin >> T;
    while(T--) {
        int N, Q;
        cin >> N;
        if(N == 1) {
            printf("1\n");
            continue;
        }
        reset(N);
        for(int i = 0; i < N-1; i++) {
            int u, v;
            cin >> u >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }
        tree[1].push_back(0);
        dfs(1, 0);
        cin >> Q;
      
        for(int i = 0; i < Q; i++) {
            int x, y;
            cin >> x >> y;            
            printf("%lld\n", (long long)(cnt[x]) * (long long)(cnt[y]));
        }

    }
}