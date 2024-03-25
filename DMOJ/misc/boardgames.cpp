#include <bits/stdc++.h>
using namespace std;

const int size = (int)(1e7);
int N, M, dist[size];
bool vis[size];

int bfs(int N, int M){
  for(int i = 0; i < size; i++){
    dist[i] = size;
  }
  list<int> q;
  dist[N] = 0;
  vis[N] = true;
  q.push_back(N);
  while(!q.empty() && !vis[M]){
    int cur = q.front();    
    q.pop_front();
    if(vis[M] || cur == M) break;
    if(cur < 0) continue;
    if(!vis[cur*3] && cur * 3 < size && cur > 0){
      q.push_back(cur*3);
      vis[cur*3] = true;
      dist[cur*3] = min(dist[cur*3], dist[cur] + 1);
    }
    if(cur % 2 == 0 && !vis[cur/2]){
      q.push_back(cur/2);
      vis[cur/2] = true;
      dist[cur/2] = min(dist[cur/2], dist[cur] + 1);    
    }
    if(!vis[cur-3] && cur - 3 > 0){
      q.push_back(cur-3);
      vis[cur-3] = true;
      dist[cur-3] = min(dist[cur-3], dist[cur] + 1);
    }
    if(!vis[cur-1] && cur - 1 > 0){
      q.push_back(cur-1);
      vis[cur-1] = true;
      dist[cur-1] = min(dist[cur-1], dist[cur] + 1);
    }
  }
  return dist[M];
}

int main() {
  scanf("%d %d", &N, &M);
  cout << bfs(N, M) << endl;
}