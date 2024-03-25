#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5;
typedef long long ll;
int MIN, MAX, N;
ll DP[MAXN];
#define pb push_back

vector<int> M = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000};

bool valid (int x, int y, int z) { 
  if(x <= y && y <= z) return true;
  return false;
}

ll findPath () {
  for(int i = 1; i < M.size(); i++){
    for(int j = 0; j < i; j++){
      if(valid(MIN, M[i] - M[j], MAX)) {
        DP[i] += DP[j];
      }
    }
  }
  return DP[M.size() - 1];
}

int main() {
  scanf("%d %d %d", &MIN, &MAX, &N);
  for(int i = 1, D; i <= N; i++) {
    scanf("%d", &D);
    M.pb(D);
  }
  sort(M.begin(), M.end());
  DP[0] = 1;
  printf("%lld\n", findPath());
}