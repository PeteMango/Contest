#include <bits/stdc++.h>
using namespace std;

const int size = (int)(1e5 + 5);
int N, K, arr[size], dp[size];

int main() {
    scanf("%d %d", &N, &K);
    for(int i = 1; i <= N; i++){
        scanf("%d", &arr[i]);
        dp[i] = 1e9;
    }
    dp[1] = 0;
    for(int i = 1; i <= N; i++){
        for(int j = 0; j <= K && i + j <= N; j++){
            dp[i + j] = min(dp[i + j], dp[i] + abs(arr[i]-arr[i+j]));
        }
    }
    /*
    for(int i = 1; i <= N; i++){
        cout << dp[i] << endl;
    }
    */
    printf("%d\n", dp[N]);
}
