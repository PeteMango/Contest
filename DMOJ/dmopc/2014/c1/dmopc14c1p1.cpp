#include <bits/stdc++.h>
using namespace std;

string a, b;

int main () {
    cin >> a >> b;
    if(b[b.length() - 1] == 'e') {
        cout << a << "-tu la " << b << " ?" << endl;
    }
    else if(b[b.length() - 1] == 's') {
        cout << a << "-tu les " << b << " ?" << endl;
    }
    else {
        cout << a << "-tu le " << b << " ?" << endl;
    }
}
