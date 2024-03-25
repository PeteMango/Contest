#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 100000
 
int N, A, x[MAXN], y[MAXN], ciD[MAXN], minL[MAXN], maxR[MAXN];
 
bool cmp(int a, int b) {
	if(x[a] == x[b]) {
    return (y[a] < y[b]);
  }
	return (x[a] < x[b]);
}
  
int main() {
	scanf("%d", &N);
	for(int i = 0; i < N; i++){
		scanf("%d%d", &x[i], &y[i]);
		ciD[i] = i;
	}
	sort(ciD, ciD+N, cmp);
	minL[0] = y[ciD[0]];
	for(int i = 1; i < N; i++) {
		minL[i] = min(minL[i-1], y[ciD[i]]);
  }
	maxR[N-1] = y[ciD[N-1]];
	for(int i = N-2; i >= 0; i--) {
		maxR[i] = max(maxR[i+1], y[ciD[i]]);
  }
	for(int i = 0; i < N-1; i++) {
		if(minL[i] > maxR[i+1]) {
			A++;
    }
  }
	printf("%d\n", A+1);
}