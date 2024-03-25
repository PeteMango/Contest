#include <bits/stdc++.h>
using namespace std;
int T;

void solve () {
    int r, c;
    cin >> r >> c;

    string ret = "";
    char input[25][25];
    for(int i = 0; i < r; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < c; j++) {
            input[i][j] = s[j];
        }
    }

    for(int i = 0; i < c; i++) {
        for(int j = 0; j < r; j++) {
            if(ret.length() == 0 && input[j][i] == 'v') {
                ret += 'v';
                break;
            }
            if(ret.length() == 1 && input[j][i] == 'i') {
                ret += 'i';
                break;
            }
            if(ret.length() == 2 && input[j][i] == 'k') {
                ret += 'k';
                break;
            }
            if(ret.length() == 3 && input[j][i] == 'a') {
                ret += 'a';
                break;
            }
        }
    }

    if(ret == "vika") {
        printf("yes\n");
    }
    else {
        printf("no\n");
    }
}

int main () {
    cin >> T;
    while(T--) {
        solve();
    }
}