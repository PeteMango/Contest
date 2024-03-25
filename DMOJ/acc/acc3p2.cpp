#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int N;
LL inX, inY, ans = 1e18;
vector<LL> X, Y, oX, oY;


LL check(LL a, LL b, vector<LL>& A, vector<LL>& B) {
	LL tot = 0;
	for(int i = 0; i < A.size(); i++){
		tot += max(abs(A[i] - a), abs(B[i] - b));
	}
	return tot;
}

int main(){
  scanf("%d", &N);
	for(int i = 1; i <= N; i++){
		scanf("%lld %lld", &inX, &inY);
		oX.push_back(inX);
		oY.push_back(inY);
		X.push_back(inX+inY);
		Y.push_back(inX-inY);
	}

	sort(X.begin(),X.end());
	sort(Y.begin(),Y.end());
	LL s1 = X[N/2],s2 = Y[N/2];
	LL x0 = (s1+s2)/2;
	LL y0 = s1 - x0;

	for(int i = -2; i <= 2; i++){
		for(int j = -2; j <= 2; j++){
			ans = min(ans, check(x0 + i, y0 + j, oX, oY) );
		}
	}
	printf("%lld\n", ans);     
}