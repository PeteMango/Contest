#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;

void multiply(ll F[2][2], ll t[2][2]){
    ll a, b, c, d;
    a = (F[0][0] * t[0][0] + F[0][1] * t[1][0]) % 1000000007;
    b = (F[0][0] * t[0][1] + F[0][1] * t[1][1]) % 1000000007;
	c = (F[1][0] * t[0][0] + F[1][1] * t[1][0]) % 1000000007;
	d = (F[1][0] * t[0][1] + F[1][1] * t[1][1]) % 1000000007;

	F[0][0] = a; F[0][1] = b; F[1][0] = c; F[1][1] = d;
}

void power(ll F[2][2], ll N){
    if(N == 0 || N == 1){
        return;
    }
    ll t[2][2] = {{1,1},{1,0}};
    power(F, (N / 2));
    multiply(F, F);
    if(N % 2 != 0){
        multiply(F, t);
    }
}

ll fib(ll N){
    ll F[2][2] = {{1,1},{1,0}};
    if(N == 0) return 0;
    power(F, N);
    return F[0][1];
}

ll N;
int main() {
  cin >> N;
  cout << fib(N) << endl;
}
