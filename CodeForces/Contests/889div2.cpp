#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;

bool isSorted (vector<int> v) {
    for(int i = 1; i < v.size(); i++) {
        if(v[i] < v[i-1]) {
            return false;
        }
    }
    return true;
}

void testMoves (vector<pair<int, int> >moves, vector<int> v) {
    printf("TESTING MOVES\n");
    for(int i = 0; i < moves.size(); i++) {
        v[moves[i].first-1] += v[moves[i].second-1];
    }
    for(int i = 0; i < v.size(); i++) {
        printf("%d ", v[i]);
    }
    cout << endl;
}

void printMoves (vector<pair<int, int> >moves) {
    printf("%lu\n", moves.size());
    for(int i = 0; i < moves.size(); i++) {
        printf("%d %d\n", moves[i].first+1, moves[i].second+1);
    }
}

void solveHasPos (vector<int> v, int n) {
    vector<pair<int, int> > moves;
    int posIdx = -1;
    for(int i = 0; i < n; i++) {
        if(v[i] > 0) {
            posIdx = i;
            break;
        }
    }
    while(v[posIdx] <= 20) {
        v[posIdx] += v[posIdx];
        moves.push_back(make_pair(posIdx, posIdx));
    }
    v[0] += 2 * v[posIdx];
    for(int i = 0; i < 2; i++) {
        moves.push_back(make_pair(0, posIdx));
    }

    for(int i = 0; i < n; i++) {
        while(v[i] < v[i-1]) {
            v[i] += v[i-1];
            moves.push_back(make_pair(i, i-1));
        }
    }
    printMoves(moves);
}

void solveAllNeg (vector<int> v, int n) {
    vector<pair<int, int> >moves;
    for(int i = n-1; i >= 1; i--) {
        moves.push_back(make_pair(i-1, i));
    }
    printMoves(moves);
}

void solve () {
    int n, allNeg = 0;
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i];
        if(v[i] > 0) {
            allNeg = 1;
        }
    }
    if(n == 1 || isSorted(v)) {
        printf("%d\n", 0);
        return;
    }
    if(n == 2) {
        if(v[0] > v[1]) {
            printf("%d\n%d %d\n", 1, 2, 1);
        }
        else {
            printf("%d\n", 0);
        }
        return;
    }
    if(allNeg == 1) {
        solveHasPos(v, n);
    }
    else {
        solveAllNeg(v, n);
    }
}

int main () {
    cin >> T;
    while(T--) {
        solve();
    }
}