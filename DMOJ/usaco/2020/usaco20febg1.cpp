#include <bits/stdc++.h>
using namespace std;
const int MM = 1e5 + 5;

int N, M, C, s[MM], inDeg[MM]; 
bool vis[MM];
vector<pair<int, int>> adj[MM];
queue<int> q;
int main() {
  cin >> N >> M >> C;
  for (int i = 1; i <= N; ++i) cin >> s[i];
	for (int i = 0; i < C; ++i) {
		int a,b,x; cin >> a >> b >> x;
		adj[a].push_back({b,x}); inDeg[b] ++;
	}
	for (int i = 1; i <= N; ++i) if (!inDeg[i]) q.push(i);
	while (q.size()) {
		int x = q.front(); q.pop(); 
		vis[x] = 1; assert(s[x] <= M);
		for (auto& t: adj[x]) {
			s[t.first] = max(s[t.first],s[x]+t.second);
			if (!(--inDeg[t.first])) q.push(t.first);
		}
	}
	for (int i = 1; i <= N; ++i) {
		assert(vis[i]);
		cout << s[i] << "\n";
	}
}