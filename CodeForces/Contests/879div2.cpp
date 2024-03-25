#include <bits/stdc++.h>
using namespace std;
int T;

int main () {
    cin >> T;
    while(T--) {
        int n, numPos=0, numNeg=0, ret=0;
        cin >> n;
        for(int i = 0, x; i < n; i++) {
            cin >> x;
            if(x > 0) {
                numPos++;
            }
            else {
                numNeg++;
            }
        }
        if(numNeg > numPos) {
            int numSubtract = ((numNeg - numPos) % 2 == 0)? ((numNeg-numPos)/2):((numNeg-numPos)/2)+1;
            ret += numSubtract;
            numNeg -= numSubtract;
        }
        if(numNeg % 2 == 1) {
            ret++;
        }
        cout << ret << endl;
    }  
}