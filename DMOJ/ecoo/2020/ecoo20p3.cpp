#include <bits/stdc++.h>
using namespace std;
#define pb push_back
const int MM = 505;
int T, N, H, W;
vector<int> solved;

int main () {
  cin >> T;
  for(int tstcase = 1; tstcase <= T; tstcase++) {
    cin >> N;
    solved.clear();
    for(int numb = 1; numb <= N; numb++) {
      cin >> H >> W;
      char Grid[MM][MM];
      for(int i = 0; i < H; i++) {
        for(int j = 0; j < W; j++) {
          cin >> Grid[i][j];
        }
      }
      int startx=0, starty=0, endx=H-1, endy=W-1;
      for(int i = 0; i < H; i++) {
        bool asterisk = false;
        for(int j = 0; j < W; j++) {
          if(Grid[i][j] == '*') {
            asterisk = true;
          }
        }
        if(asterisk) {
          startx = i;
          break;
          }
        }
        for(int j = 0; j < W; j++) {
          bool asterisk = false;
          for(int i = 0; i < H; i++) {
            if(Grid[i][j] == '*') {
              asterisk = true;
            }
          }
          if(asterisk) {
            starty = j;
            break;
          }
        }
        for(int i = H - 1; i >= 0; i--) {
          bool asterisk = false;
          for(int j = 0; j < W; j++) {
            if(Grid[i][j] == '*') {
              asterisk = true;
            }
          }
          if(asterisk) {
            endx = i;
            break;
          }
        }
        for(int j = W - 1; j >= 0; j--) {
          bool asterisk = false;
          for(int i = 0; i < H; i++) {
            if(Grid[i][j] == '*') {
              asterisk = true;
            }
          }
          if(asterisk) {
            endy = j;
            break;
          }
      }
      int num;
      if(starty == endy) {
        num = 1;
      }
      else if(Grid[startx][starty] == '*' && Grid[startx][endy] == '*') {
        num = 4;
      } 
      else {
        if(Grid[startx][starty] == '*') starty--;
          bool top = Grid[startx][starty + 1] == '*', bot = Grid[endx][starty + 1] == '*', mid = false;
          for(int i = startx + 1; i < endx; i++) {
            if(Grid[i][starty + 1] == '*') {
              mid = true;
              break;
            }
          }
          bool topLft = Grid[startx + 1][starty] == '*', btmLft = Grid[endx - 1][starty] == '*', topRgt = Grid[startx + 1][endy] == '*';
          if(topLft) {
            if(topRgt) {
              if(btmLft) {
               if(mid) num = 8;
                else num = 0;
              } else num = 9;
            } 
            else {
              if(btmLft) {
                num = 6;
              }
                else {
                  num = 5;
                }
              }
            } 
           else {
             if(btmLft) {
               num = 2;
             }
             else if(bot) {
               num = 3;
             }
             else {
               num = 7;
             }
          }
        }
      solved.pb(num);
    }
    for(int i = 0; i < solved.size(); i++) {
      cout << solved[i];
    }
    cout << "\n";
  }
}