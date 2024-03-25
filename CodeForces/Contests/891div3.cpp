#include <bits/stdc++.h>
using namespace std;
int T;

char plusOne (char x) {
    if(x - '0' == 9) {
        return 'x';
    }
    return (char)(((x - '0') + 1) + '0');
}

void solve () {
    string s;
    cin >> s;
    reverse(s.begin(), s.end());

    if(s.length() == 1) {
        if(s[0] - '0' >= 5) {
            printf("10\n");
        }
        else {
            cout << s << endl;
        }
        return;
    }

    for(int i = 0; i < s.length(); i++) {
        if(s[i] - '0' >= 5) {
            for(int j = 0; j <= i; j++) {
                s[j] = '0';
            }
            if(i == s.length() - 1) {
                s += '1';
            }
            else {
                if(plusOne(s[i] == 'x')) {
                    
                }
                s[i+1] = plusOne(s[i]);
            }
            i--;
        }
        cout << s << endl;
    }
    reverse(s.begin(), s.end());
    cout << s << endl;
}

int main () {
    scanf("%d", &T);
    while(T--) {
        solve();
    }
}