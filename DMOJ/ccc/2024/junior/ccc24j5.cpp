#include <iostream>

using namespace std;
char G[10005][10005];
int r, c, score = 0;

void dfs(int x, int y) {
  if (x < 0 || y < 0 || x >= r || y >= c) {
    return;
  }
  if (G[x][y] == '*') {
    return;
  }

  if (G[x][y] == 'S') {
    score += 1;
  } else if (G[x][y] == 'M') {
    score += 5;
  } else if (G[x][y] == 'L') {
    score += 10;
  }
  G[x][y] = '*';

  dfs(x + 1, y);
  dfs(x - 1, y);
  dfs(x, y + 1);
  dfs(x, y - 1);
  return;
}

int main() {
  cin >> r >> c;

  for (int i = 0; i < r; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < c; j++) {
      G[i][j] = s[j];
    }
  }

  int x, y;
  cin >> x >> y;

  dfs(x, y);
  printf("%d\n", score);
}
