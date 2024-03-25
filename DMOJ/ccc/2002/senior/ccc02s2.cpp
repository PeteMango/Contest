#include <bits/stdc++.h>
using namespace std;

int A, B, M, N, D;

void reduce () {
    for(int i = 2; i <= min(N, B); i++) {
        if(N%i == 0 && B%i == 0) {
            N /= i;
            B /= i;
            i--;
        }
    }
}

int main () {
    cin >> A >> B;
    if(A % B == 0) {
        cout << A/B << endl;
    }
    else {
        M = A / B;
        N = A % B;
        reduce();
        if(M == 0) {
            cout << N << "/" << B << endl;
        }
        else {
            cout << M << " " << N << "/" << B << endl;
        }
    }
}
