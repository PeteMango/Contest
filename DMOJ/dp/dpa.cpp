#include <bits/stdc++.h>
using namespace std;

const int size = (int)(1e5 + 5);
int N, arr[size], dp[size];

int main() {
    scanf("%d", &N);
    for(int i = 1; i <= N; i++){
        scanf("%d", &arr[i]);
    }
    dp[2] = abs(arr[1]-arr[2]);
    for(int i = 3; i <= N; i++){
        dp[i] = min(dp[i-1] + abs(arr[i]-arr[i-1]), dp[i-2] + abs(arr[i]-arr[i-2]));
    }
    /*
    for(int i = 1; i <= N; i++){
        cout << dp[i] << endl;
    }
    */
    printf("%d\n", dp[N]);
}

