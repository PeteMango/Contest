#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;
 
ll min(ll a, ll b) {
    return (a<b)? a:b;
}
 
int main () {
    cin >> T;
    while(T--) {
        ll n, k, mx = 0;
        cin >> n >> k;
        vector<ll> v (n);
        for(int i = 0; i < n; i++) {
            cin >> v[i];
            v[i]--;
        }
        if(n == 1 && v[0] == 0) {
            cout << (k+1) << endl;
            continue;
        }
        if(v[0] != 0) {
            cout << 1 << endl;
            continue;
        }
        mx = v[n-1];
        vector<ll> nums;
        for(int i = 1; i <= mx + 5; i++) {
            nums.push_back(i);
        }
 
        for(int i = 0; i < min(n+1, k); i++) {
            for(int j = 0; j < v.size(); j++) {
                nums[v[j]] = -1;
            }
            for(int j = 0; j < nums.size(); j++) {
                if(nums[j] == -1) {
                    nums.erase(nums.begin() + j);
                    j--;
                }
            }
            sort(nums.begin(), nums.end());
            mx = nums[nums.size() - 1];
            for(ll j = mx+1; j <= mx + n; j++) {
                nums.push_back(j);
            }
        }
        if(k <= n) {
            printf("%lld\n", (long long)(nums[0]));
        }
        else {
            printf("%lld\n", (long long)(nums[0] + ((k-n-1) * n)));
        }
    }
}