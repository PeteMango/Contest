#include <bits/stdc++.h>
using namespace std;
int T;
typedef long long ll;

int greaterThan (int a, int b) {
    return a > b? a:b;
}

int maxInVector (vector<int> v) {
    int mx = -1;
    for(int i = 0; i < v.size(); i++) {
        mx = greaterThan(mx, v[i]);
    }
    return mx;
}

bool canIncrease (vector<int> v, int index, int toIncrease, int k) {
    // cout << "Index: " << index << " toIncrease: " << toIncrease << " k: " << k << endl;
    if(k <= 0 || index >= v.size()) {
        return false;
    }
    if(toIncrease == 0) {
        return true;
    }
    return canIncrease(v, index+1, v[index] - v[index + 1] + toIncrease - 1, k - (v[index] - v[index + 1] + toIncrease - 1));
}

void solve () {
    int n, k, biggest = -1;
    scanf("%d %d", &n, &k);
    vector<int> v(n);

    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }

    

    for(int i = 0; i < n; i++) {
        for(int j = 1; j <= k; j++) {
            if(canIncrease(v, i, j, k)) {
                biggest = greaterThan(biggest, v[i] + j);
            }
            else {
            }
        }
    }
    printf("%d\n", biggest);
}

int main () {
    cin >> T;
    while(T--) {
        solve();
    }
}
