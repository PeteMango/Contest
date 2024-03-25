#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define endl '\n'

const int MM = 100005;
int N, fact[MM];
vector<int> v[MM];

int main () {
  for(int i = 1; i < MM; i++) fact[i] = 1;
  for(int i = 2; i < MM; i++) {
    for(int j = i; j < MM; j += i) {
      fact[j]++;
    }
  }
  for(int i = 1; i < MM; i++) {
    v[fact[i]].pb(i);
  }
  cin >> N;
  for(int i = 1, K, A, B; i <= N; i++) {
    cin >> K >> A >> B;
    if(v[K].empty() || v[K].back() < A) {
      cout << "0" << endl;
      continue;
    }
    vector<int>::iterator L = lower_bound(v[K].begin(), v[K].end(), A), R = prev(upper_bound(v[K].begin(), v[K].end(), B));
    cout << (R-L+1) << endl;
  }
}