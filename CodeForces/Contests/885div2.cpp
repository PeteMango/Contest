#include <bits/stdc++.h>
using namespace std;

#define pb push_back

const int N = 2e5 + 5;

int n, k, t, a[N], pre[N];
vector<int> pos[N];

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> t;
    while(t--) {
        cin >> n >> k;
        for(int i = 1; i <= k; i++) pos[i].clear();
        for(int i = 1; i <= n; i++) {
            cin >> a[i];
            pos[a[i]].pb(i);
        }
        int ans = n;
        for(int i = 1; i <= k; i++) {
            sort(pos[i].begin(), pos[i].end());
            for(int j = 0; j < pos[i].size(); j++) {
                pre[j + 1] = pre[j] + (j ? pos[i][j - 1] : 0);
            }
            for(int j = 0; j < pos[i].size(); j++) {
                int k = lower_bound(pos[i].begin(), pos[i].end(), pos[i][j] - j) - pos[i].begin();
                int cost = pre[j + 1] - pre[k] + (k * (k + 1) / 2) + ((n - pos[i][j]) * (j - k + 1));
                ans = min(ans, cost);
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
