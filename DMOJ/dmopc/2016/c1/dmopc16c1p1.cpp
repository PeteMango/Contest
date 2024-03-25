#include <bits/stdc++.h>
using namespace std;

const int MAXN = 35;
int N, A[MAXN], CNT;

int main() {
    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
        if(A[i] == i || A[i] % 2 == i % 2) CNT++;
    }
    printf("%d", CNT);
}
