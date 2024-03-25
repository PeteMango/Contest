#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
typedef long long ll;
int N, A[MAXN], B[MAXN];
ll T;
char S[MAXN];

void step (int K) {
    int pos1 = (1LL << K)%N, pos2 = (N-pos1)%N;
    for(int i = 0; i < N; i++) {
        B[i] = A[(i + pos1)%N]^A[(i+pos2)%N];
    }
    memcpy(A, B, sizeof A);
}

int main () {
    scanf("%d %lld", &N, &T);
    scanf("%s", S);
    for(int i = 0; i < N; i++) {
        A[i] = S[i] - '0';
    }
    for(int i = 60; i >= 0; i--) {
        if((T>>i)&1) {
            step(i);
        }
    }
    for(int i = 0; i < N; i++) {
        printf("%d", A[i]);
    }
    printf("\n");
}
