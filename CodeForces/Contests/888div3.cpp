#include <bits/stdc++.h>
using namespace std;
int T;

void solve () {
    int n;
    vector<int> a, b;
    cin >> n;
    for(int i = 0, x; i < n; i++) {
        cin >> x;
        a.push_back(x);
        b.push_back(x);
    }
    sort(b.begin(), b.end());   
    for(int i = 0; i < n; i++) {
        if(a[i] % 2 != b[i] % 2) {
            printf("NO\n");
            return;
        }
    }
    printf("YES\n");
}

int main () {
    cin >> T;
    while(T--) {
        solve();
    }
}