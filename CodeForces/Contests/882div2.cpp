#include <bits/stdc++.h>
using namespace std;
int T;

int max (int a, int b) {
    return a>b? a:b;
}

int main () {
    cin >> T;
    while(T--) {
        int n, bitwiseAnd, numGroups = 1;
        vector<int> v;
        cin >> n;

        for(int i = 0, x; i < n; i++) {
            cin >> x;
            v.push_back(x);
        }
        if(n == 1) {
            cout << 1 << endl;
            continue;
        }

        bitwiseAnd = v[0];
        for(int i = 1; i < n; i++) {
            bitwiseAnd &= v[i];
        }
        
        if(bitwiseAnd > 0) {
            cout << 1 << endl;
            continue;
        }
        
        bitwiseAnd = v[0];
        for(int i = 0; i < n; i++) {
            bitwiseAnd &= v[i];
            if(bitwiseAnd == 0 ) {
                if(i == n-1) {
                    break;
                }
                numGroups++;
                bitwiseAnd = v[i+1];
            }
        }
        if(bitwiseAnd != 0) {
            numGroups--;
        }
        cout << max(numGroups, 1) << endl;
    }
}