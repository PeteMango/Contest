#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
int N, M, S[MAXN], D[MAXN];
string s;

int main () {
    scanf("%d", &N);
    for(int i = 1; i <= N; i++) {
        cin >> s;
        S[i] = s.length();
    }
    scanf("%d", &M);
    for(int i = 1; i <= N; i++) {
        int smallest = 0x3f3f3f3f, idx = -1;
        for(int j = 1; j <= M; j++) {
            if(D[j] < smallest) {
                smallest = D[j];
                idx = j;
            }
        }
        printf("%d\n", idx);
        D[idx] += S[i];
    }
}
