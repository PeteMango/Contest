#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 100005

int N, M, cnT, f[MAXN], s[MAXN], occ[MAXN], ans[MAXN];

int main() {
	scanf("%d%d", &N, &M);
	for(int i = 0; i < N; i++) {
		scanf("%d%d", &f[i], &s[i]);
  }
	for(int i = N-1; i >= 0; i--) {
		int j = i, pos = f[i];
		while(true) {
			if(occ[pos] == 0) {
				occ[pos] = j;
				cnT++;
				break;
			}
			else if(occ[pos] < j) {
				break;
      }
			else {
				int k = occ[pos];
				occ[pos] = j;
				if(pos == s[k])
					break;
				j = k;
				pos = s[k];
			}
		}
		ans[i] = cnT;
	}
	for(int i = 0; i < N; i++) {
		printf("%d\n", ans[i]);
  }
}