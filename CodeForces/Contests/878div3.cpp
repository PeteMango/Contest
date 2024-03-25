#include <bits/stdc++.h>
using namespace std;
int T;

int main () {
    cin >> T;
    while(T--) {
        int n, l=-1, r=1e9+5, m;
        vector<int> v;
        cin >> n;
        for(int i = 0, x; i < n; i++) {
            cin >> x;
            v.push_back(x);
        }
        sort(v.begin(), v.end());
        if(n <= 3) {
            cout << 0 << endl;
            continue;
        }

        while(r - l > 1) {
            int i = 0, j = n-1;
            m = (l+r)/2;
            while(i + 1 < n && v[i + 1] - v[0] <= 2 * m) {
                i++;
            }
            while(j - 1 >= 0 && v[n-1] - v[j-1] <= 2 * m) {
                j--;
            }
            i++; j--;

            /* too much for carver 1 if i > j or if the amount for middle carver is too little */
            if(i > j || v[j] - v[i] <= 2 * m) {
                r = m;
            }
            else {
                l = m;
            }
        }
        cout << r << endl;
    }
}