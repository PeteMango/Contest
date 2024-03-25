#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
int N, K, cnt[MAXN], arr[MAXN], r;
long long d, t;

int main() {
    scanf("%d %d", &N, &K);
    for(int i = 0; i < N; i++) {
      scanf("%d", &arr[i]);
    }
    for(int l = 0; l < N; l++) {
        while(r < N && d < K) {
            if(cnt[arr[r]] == 0) d++;
            cnt[arr[r]]++;
            r++;
        }

        if(d < K) break;

        t += N-r+1;
        cnt[arr[l]]--;
        if(cnt[arr[l]] == 0) d--;
    }
    printf("%lld\n", t);
}