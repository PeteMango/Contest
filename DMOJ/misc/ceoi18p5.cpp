#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
vector<int> sol;
int N;

void fun (int cur, int fact, int sum) {
  sol.push_back(sum + cur - 1);
  for(int i = fact; i*i <= cur; i++) {
    if(cur % i == 0) {
      fun(cur/i, i, sum + i - 1);
    }
  }
}

int main() {
  cin  >> N;
  fun(N, 2, 0);
  sort(sol.begin(), sol.end());
  int tot = unique(sol.begin(), sol.end())-sol.begin();
  cout << tot << "\n";
  for(int i = 0; i < tot; i++) {
    cout << sol[i] << " ";
  }
  cout << "\n";
}