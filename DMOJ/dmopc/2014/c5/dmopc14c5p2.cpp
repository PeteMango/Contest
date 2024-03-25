#include <bits/stdc++.h>
using namespace std;

int N, S, E, M;

int main () {
    cin >> N;
    for(int i = 1; i <= N; i++) {
        cin >> S >> E;
        if(abs(E - S) > M) {
            M = abs(E - S);
        }
    }
    cout << M << endl;
}
