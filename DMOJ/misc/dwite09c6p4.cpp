#include <bits/stdc++.h>
using namespace std;


int minCoins(int coins[], int M, int T){
    int table[T + 1];
    for(int i = 1; i <= T; i++){
        table[i] = 1e9;

    }
    table[0] = 0;
    for(int i = 1; i <= T; i++){
        for(int j = 0; j < M; j++){
            if(coins[j] <= i){
                int cur = table[i - coins[j]];
                if(cur != 1e9 && cur + 1 < table[i]){
                    table[i] = cur + 1;
                }
            }
        }
    }
    return table[T];
}

int main(){
    for(int i = 0, M, T, arr[105]; i < 5; i++){
        scanf("%d %d", &T, &M);
        for(int j = 0; j < M; j++){
            scanf("%d", &arr[j]);
        }
        cout << minCoins(arr, M, T) << endl;
    }
}
