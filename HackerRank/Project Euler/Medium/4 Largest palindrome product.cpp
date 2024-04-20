#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


bool isPalidrome(int N) {
    string s = to_string(N);
    for(int i = 0; i < s.length() / 2; i++) {
        if(s[i] != s[s.length() - 1 - i]) {
            return false;
        }
    }
    return true;
}

bool isProduct(int N) {
    for(int i=100; i<=999;i++) {
        if(N % i == 0 && N/i >= 100 && N/i <= 999) {
            return true;
        }
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        int N;
        cin >> N;
        for(int i = N-1; i >= 10000; i--) {
            if(isPalidrome(i) && isProduct(i)) {
                cout << i << "\n";
                break;
            }
        }
    }
    return 0;
}
