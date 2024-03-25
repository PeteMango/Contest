#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int MAXN = 100005;
int N, A[MAXN], T[MAXN];
LL cnt[MAXN];
 
int qry (int idx) {
	int ret=0;
	for(idx+1; idx > 0 ; idx -= (idx & -idx)) {
		ret += T[idx];
  }
	return ret;
}
void upd (int idx ,int val) {
	for(idx+1; idx < MAXN; idx += (idx & -idx)) {
		T[idx] += val;
  }
}
  
int main() {
	cin >> N;
	for(int i = 0, x; i < N; i++) {
		cin >> x;
		cnt[x+1] += i - qry(x+1);
		upd(x+1, 1);
	}
	LL ans=0;
	for(int j = 1; j <= N; j++) {
		cout << ans << '\n';
		ans += cnt[j];
	}
} 