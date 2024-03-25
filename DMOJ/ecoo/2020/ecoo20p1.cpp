#include <bits/stdc++.h>
using namespace std;
int T;
map<string, int> mp;

void initializeMap () {
  mp["C"] = 0; 
  mp["C#"] = 1;
  mp["D"] = 2;
  mp["D#"] = 3;
  mp["E"] = 4;
  mp["F"] = 5;
  mp["F#"] = 6;
  mp["G"] = 7;
  mp["G#"] = 8;
  mp["A"] = 9;
  mp["A#"] = 10;
  mp["B"] = 11;
}

int findDif (string a, string b) {
  if(mp[a] > mp[b]) {
    return mp[b]-mp[a]+12;
  }
  return mp[b]-mp[a];
}

int main() {
  initializeMap();
  cin >> T;
  for(int i = 1; i <= T; i++) {
    string a, b, c, d;
    cin >> a >> b >> c >> d;
    if (findDif(a, b) == 4 && findDif(b, c) == 3 && findDif(c, d) == 3) {
      cout << "root\n";
    } 
    else if (findDif(a, b) == 3 && findDif(b, c) == 3 && findDif(c, d) == 2) {
      cout << "first\n";
    } 
    else if (findDif(a, b) == 3 && findDif(b, c) == 2 && findDif(c, d) == 4) {
      cout << "second\n";
    } 
    else if (findDif(a, b) == 2 && findDif(b, c) == 4 && findDif(c, d) == 3) {
      cout << "third\n";
    } 
    else {
      cout << "invalid\n";
    }
  }
}

/*
4-3-3 --> Root
3-3-2 --> first
3-2-4 --> second
2-4-3 --> third
else invalid
*/

