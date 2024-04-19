#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;
    deque<int> dq;
    while (q--) {
        int cmd;
        cin >> cmd;
        if(cmd == 1) {
            int x;
            cin >> x;
            dq.emplace_back(x);
        }
        else if(cmd == 2) {
            dq.pop_front();
        }
        else if(cmd == 3) {
            cout << dq.front() << "\n";
        }
        else {
            return -1;
        }
    }
    return 0;
}
