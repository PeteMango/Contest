#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAXN = 16, MAXL = 26;

ll fact[MAXN], ANS;
int N, K, num[MAXL];
string s;

ll generate () {
  ll ret = fact[N];
  for(int i = 0; i < 26; i++) {
    ret /= fact[num[i]];
  }
  return ret;
}

int main() {
  scanf("%d %d", &N, &K);
  fact[0] = 1;
  for(int i = 1; i <= 15; i++) {
    fact[i] = fact[i - 1] * i;
  }
  cin >> s;
  for(int i = 0; i < N; i++) {
    if(s[i] != '*') {
      num[s[i]-'a']++;
    }
  }
  if(K == 0) { 
    printf("%lld", generate());
  }
  else if(K == 1) {
    for(int i = 0; i < 26; i++) {
      num[i]++;
      ANS += generate();
      num[i]--;
    }
    printf("%lld", ANS);
  }
  else {
    for(int i = 0; i < 26; i++) {
      for(int j = i; j < 26; j++) {
        num[i]++;
        num[j]++;
        ANS += generate();
        num[i]--;
        num[j]--;
      }
    }
    printf("%lld\n", ANS);
  }
} 