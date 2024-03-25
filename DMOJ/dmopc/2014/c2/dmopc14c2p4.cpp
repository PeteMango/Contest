#include <bits/stdc++.h>
using namespace std;

int N, Q, psa[1000005];

int main(){
    cin >> N;
    for(int i = 1, t; i <= N; i++){
        scanf("%d", &t);
        psa[i] = psa[i - 1] + t;
    }
    cin >> Q;
    for(int i = 0, a, b; i < Q; i++){
        scanf("%d %d", &a, &b);
        cout << (psa[b + 1] - psa[a]) << endl;
    }
}
