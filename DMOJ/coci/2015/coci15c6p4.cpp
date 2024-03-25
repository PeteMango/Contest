#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;
int N, dp[1 << 20], MOD = (int)1e9;
vector<pi> a;

int main(){
    scanf("%d", &N);
    for(int i = 1; i <= N; i++){
        for(int j = i + 1; j <= N; j++){
            if(__gcd(i, j) == 1) a.push_back({i - 1, j - 1});
        }
    }
    dp[0] = 1; N--;
    for(pi e : a){
        for(int pre = (1 << N) - 1; pre >= 0; pre--){
            int msk = ((1 << e.second) - 1) - ((1 << e.first) - 1), cur = msk|pre;
            dp[cur] = (dp[cur] + dp[pre]) % MOD;
        }
    }
    printf("%d\n", dp[(1 <<N) - 1]);
}
