#include <bits/stdc++.h>
using namespace std;

#define pb push_back

const int MAXN = 105;
int N, CNT = 0;
string S;
bool flag;

int main () {
    cin >> N >> S;
    for(int i = 0; i < N; i++) {
        if(S[i] == 'X') {
            flag = true;
        }
        if(S[i] == 'O' && flag) {
            CNT++;
            flag = false;
        }
    }
    if(S[0] == 'X') CNT--;
    cout << CNT + 1 << endl;
    for(int i = 0; i < N; i++) {
        if(S[i] == 'X') {
            cout << endl;
        }
        else cout << S[i];
    }
}
