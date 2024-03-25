#include <bits/stdc++.h>
using namespace std;
int N, top = -1;
pair <int, int> buff[1000010];

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    for (int i = 0, ic = 0, h; i < N; i++) {
        cin >> h;
        while(top >= 0 && buff[top].first <= h) {
            top--;
        }
        if (top >= 0) ic = i - buff[top].second;
        else if (i!=0) ic = i;
        buff[++top] = make_pair(h, i);
        cout << ic << " "; 
    }
}