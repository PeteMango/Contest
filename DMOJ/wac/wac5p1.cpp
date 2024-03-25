#include <bits/stdc++.h>
using namespace std;
const int MM = 1e6 + 5;
int N, mx = -1, sum = 0, a[MM];

int main () {
	cin >> N;
	for(int i = 1, x; i <= N; i++) {
		cin >> x;
		a[x]++;
		if(x > mx) mx = x;
	}
	for(int i = mx; i > 1; i--) {
		if(a[i] <= 0) continue;
		for(int x = 1; x <= a[i]; x++){
			for(int j = i-1; j >= 1; j--) {
				a[j]--;
			}
		}
	}
	for(int i = 1; i <= mx; i++) {
		if(a[i] > 0) {
			sum += a[i] * i;
		}
	}
	cout << sum << "\n";
}

