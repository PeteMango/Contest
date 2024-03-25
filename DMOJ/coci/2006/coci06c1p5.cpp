#include <bits/stdc++.h>
using namespace std;
// https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/tutorial/
int N;
double tsk[20][20], dp[(1<<20)];
int main(){
    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            scanf("%lf", &tsk[i][j]);
            tsk[i][j] *= 0.01;
        }
    }
    /*
    cout << "N: " << N << endl;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << tsk[i][j] << " ";
        }
        cout << endl;
    }
    */
    dp[0] = 1.0;
    for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			for(int mask = 0; mask < (1<<N); mask++){
				if(mask&(1 << j) || __builtin_popcount(mask) != i) continue;
				int cur = (mask|(1<<j));
				dp[cur] = max(dp[cur], tsk[j][i]*dp[mask] );
			}
		}
	}
    printf("%.6lf\n", dp[(1<<N)-1]*100.0);
}
