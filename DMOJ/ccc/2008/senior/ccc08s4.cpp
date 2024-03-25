#include <bits/stdc++.h>
using namespace std;

vector<int> cards(4);
int N, ans = 0;

void solve(int num, int lvl) {
	if (lvl == 4) {
		if (num > ans && num <= 24) {
			ans = num;
    }
		return;
	}
	solve(num + cards[lvl], lvl + 1);
	solve(num - cards[lvl], lvl + 1);
	solve(num * cards[lvl], lvl + 1);
	if (num % cards[lvl] == 0) {
		solve(num / cards[lvl], lvl + 1);
  }
	if (lvl == 1 || lvl == 2){
		solve(num + (cards[lvl] * cards[lvl + 1]), lvl + 2);
		solve(num - (cards[lvl] * cards[lvl + 1]), lvl + 2);
		if (cards[lvl] % cards[lvl + 1] == 0){
			solve(num + (cards[lvl] / cards[lvl + 1]), lvl + 2);
			solve(num - (cards[lvl] / cards[lvl + 1]), lvl + 2);
		}
		solve(num * (cards[lvl] + cards[lvl + 1]), lvl + 2);
		solve(num * (cards[lvl] - cards[lvl + 1]), lvl + 2);
		if (num % cards[lvl] + cards[lvl + 1] == 0) {
			solve(num / (cards[lvl] + cards[lvl + 1]), lvl + 2);
    }
		if (num % cards[lvl] - cards[lvl + 1] == 0) {
			solve(num / (cards[lvl] - cards[lvl + 1]), lvl + 2);
    }
	}
}

int main() {
  cin.sync_with_stdio(0);
	cin.tie(0);

  cin >> N;
  for(int x = 0; x < N; x++) {
    for(int i = 0; i < 4; i++) {
      cin >> cards[i];
    }
    sort(cards.begin(), cards.end());
		do
		{
			solve(cards[0], 1);
		} while (next_permutation(cards.begin(), cards.end()));
    printf("%d\n", ans);
		ans = 0;
  }
}