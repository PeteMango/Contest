#include <iostream>

using namespace std;

int main() {
  string a, b;
  cin >> a >> b;

  char bef = '!', aft = '!', inv = '-';

  int freqA[26], freqB[26];
  for (int i = 0; i < 26; i++) {
    freqA[i] = freqB[i] = 0;
  }
  for (int i = 0; i < a.size(); i++) {
    freqA[a[i] - 'a']++;
  }
  for (int i = 0; i < b.size(); i++) {
    freqB[b[i] - 'a']++;
  }

  for (int i = 0; i < 26; i++) {
    if (freqB[i] > freqA[i]) {
      aft = (char)(i + (int)('a'));
    }
  }

  /* termination char to handle inv being last char */
  a += "!";
  b += "!";
  int i = 0, j = 0;
  while (i < a.size() && j < b.size()) {
    if (a[i] == b[j]) {
      i++;
      j++;
      continue;
    }

    if (b[j] == aft) {
      bef = a[i];
      i++;
      j++;
    } else {
      inv = a[i];
      i++;
    }
  }
  printf("%c %c\n%c\n", bef, aft, inv);
}
