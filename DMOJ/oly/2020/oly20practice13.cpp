#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int N, a; 
priority_queue<int> q;
LL ans;

int main () {
  cin >> N >> a;
  q.push(a);
  for(int i = 1; i < N; i++) {
    cin >> a;
    a -= i;
    q.push(a);
    if(q.top() > a) {
      ans += q.top() - a;
      q.pop();
      q.push(a);
    }
  }
  cout << ans << "\n";
}