#include <bits/stdc++.h>
using namespace std;
typedef long double LD;
int N, K;
vector<LD> dp; 
vector<int> cnt;

LD slope (int p, int q) {
  return (LD) (dp[q] - dp[p])/(q-p);
}

bool check (LD C) {
  deque<int> q;
  q.push_back(0);
  for(int i = 1; i <= N; i++) {
    while(q.size() >= 2 && slope(q[0], q[1]) >= (LD) 1.0/i) {
      q.pop_front();
    }
    dp[i] = dp[q[0]] + (LD)(i - q[0])/i - C;
    cnt[i] = cnt[q[0]] + 1;
    while(q.size() >= 2 && slope(q[q.size() - 2], q.back()) <= slope(q.back(), i)) {
      q.pop_back();
    }
    q.push_back(i);
  }
  return cnt[N] > K;
}

int main() {
  cin >> N >> K;
  dp.resize(N+1, 0); cnt.resize(N+1, 0);
  LD L = 0.0, H = 1.0;
  for(int i = 0; i < 40; i++) {
    LD M = (L+H)/2;
    if(check(M)) {
      L = M;
    }
    else H = M;
  }
  printf("%.9Lf\n", dp[N] + L*K);
}