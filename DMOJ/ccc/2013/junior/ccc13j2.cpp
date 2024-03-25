#include <bits/stdc++.h>
using namespace std;

string s;
bool flg = false;

int main () {
    cin >> s;
    for(int i = 0; i < s.length(); i++) {
        if(s[i] != 'I' && s[i] != 'O' && s[i] != 'S' && s[i] != 'H' && s[i] != 'Z' && s[i] != 'X' && s[i] != 'N') {
            flg = true;
            break;
        }
    }
    if(flg) {
        cout << "NO" << endl;
    }
    else cout << "YES" << endl;
}