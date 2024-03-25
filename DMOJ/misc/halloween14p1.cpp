#include <bits/stdc++.h>
using namespace std;
long long N, K, t;

int main(){
    cin >> N >> K;
    t = N % K;
    if(t != 0 && K - t > 0){
        if(K - t < t){
            t = K - t;
        }
    }
    if(N < K){
        t = abs(N - K);
    }
    cout << t << endl;
}
