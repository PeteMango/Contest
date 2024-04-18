#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;


int main() {
    string s = "";
    int command;
    stack<string> sk;
    while(true) {
        cin >> command;
        if(cin.fail()) {
            break;
        }
        switch(command) {
            case(1): {
                string toAdd;
                cin >> toAdd;
                sk.push(s);
                s += toAdd;
                break;
            }
            case(2): {
                sk.push(s);
                int num_remove;
                cin >> num_remove;
                s.erase(s.size() - num_remove);
                break;
            }
            case(3): {
                int k;
                cin >> k;
                cout << s[k-1] << "\n";
                break;
            }
            case(4): {
                s = sk.top();
                sk.pop();
            }
        }
    }
}
