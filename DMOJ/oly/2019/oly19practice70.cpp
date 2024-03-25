#include <bits/stdc++.h>
using namespace std;
#define pb push_back
typedef pair<int, int> pii;
const int MAXN = 1e6+5, INF = 0x3f3f3f3f;
int C, N, arr[MAXN], ans[MAXN];
vector<pii> v;
int main () {
  cin >> C >> N;
  for(int i = 1, x; i <= N; i++) {
    cin >> x; arr[x]=i;
  }
  for(int i=1; i<= C; i++) if(arr[i]) v.push_back({arr[i], i});
  sort(v.begin(), v.end());
  cout << v.size() << endl;
  for(pii i : v)
    cout << i.second << " ";
}
