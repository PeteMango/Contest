#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
int N, M, A[MAXN], T[MAXN];

int main () {
    scanf("%d", &N); M = (N-1)/2;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            scanf("%d", &T[j]);
        }
        sort(T, T+N);
        A[i] = T[M];
    }
    sort(A, A+N);
    printf("%d\n", A[M]);
}