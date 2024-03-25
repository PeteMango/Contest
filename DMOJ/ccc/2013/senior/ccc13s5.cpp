#include <bits/stdc++.h>
using namespace std;
int N, cst = 0;

int fact (int x) {
	for(int i = 2; i <= sqrt(x); i++) {
		if(x % i == 0) {
			return x/i;
		}
	}
	return 1;
}

int main () {
	cin >> N;
	while(N > 1) {
		int f = fact(N);
		cst += (N-f)/f;
		N -= f;
	}
	cout << cst << "\n";
}