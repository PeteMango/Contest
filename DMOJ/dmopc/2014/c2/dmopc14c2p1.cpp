#include <bits/stdc++.h>
using namespace std;

int D, N, L;

int main () {
    scanf("%d", &D);
    for(int i = 1; i <= D; i++) {
        scanf("%d", &N);
        if(N == 0) {
            cout << "Weekend" << endl;
        }
        else {
            int sum = 0;
            for(int j = 1; j <= N; j++) {
                scanf("%d", &L);
                sum += L;
            }
            cout << "Day " << i << ": " << sum << endl;
        }
    }
}
