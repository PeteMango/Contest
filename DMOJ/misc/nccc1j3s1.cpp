#include <bits/stdc++.h>
using namespace std;

double K, P, X;
int M;

int main () {
    cin >> K >> P >> X;
    while(K * P / X > M * M) M++;
    printf("%.3f\n", min(M*X+K*P/M,min((M-1)*X+K*P/(M-1),(M+1)*X+K*P/(M+1))));
}
