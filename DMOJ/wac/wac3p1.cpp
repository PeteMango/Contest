#include <bits/stdc++.h>
using namespace std;

int T, D, P, C;

int main () {
    cin >> T >> D >> P;
    if(T < -40) C++;
    if(D >= 15) C++;
    if(P > 50) C++;
    if(C >= 2) {
        cout << "YES" << endl;
    }
    else cout << "NO" << endl;
}