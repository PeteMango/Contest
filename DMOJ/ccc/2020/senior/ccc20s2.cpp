#include <bits/stdc++.h>
using namespace std;

#define mp make_pair

const int MAXM = 1005, MAXN = 1005;
int N, M, G[MAXM][MAXN];

bool dfs (int r, int c) {
    //cout << "currently at " << r << " " << c << endl;
    if(G[r][c] == -1 || r > M || c > N) return false;
    if(r == M && c == N) return true;
    int temp = G[r][c];
    G[r][c] = -1;
    for(int i = 1; i <= min(M, temp); i++) {
        if(temp % i == 0 && temp/i <= N) {
            if(i == r && temp/i == c) continue;
            bool f = dfs(i, temp/i);
            if(f) {
                return true;
            }
        }
    }
    return false;
}

int main () {
    scanf("%d %d", &M, &N);
    for(int i = 1; i <= M; i++) {
        for(int j = 1; j <= N; j++) {
            scanf("%d", &G[i][j]);
        }
    }
    if(dfs(1, 1)) cout << "yes" << endl;
    else cout << "no" << endl;
}