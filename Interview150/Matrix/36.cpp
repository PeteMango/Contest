#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  bool isValidSudoku(vector<vector<char>> &board) {
    int n = 9;
    auto checkRow = [&](vector<char> &rw) -> bool {
      vector<int> freq(10, 0);
      for (char c : rw) {
        if (c != '.') {
          if (++freq[c - '0'] > 1) {
            return false;
          }
        }
      }
      return true;
    };

    auto checkCol = [&](int col) -> bool {
      vector<int> freq(10, 0);
      for (int i = 0; i < n; i++) {
        if (board[i][col] != '.') {
          if (++freq[board[i][col] - '0'] > 1) {
            return false;
          }
        }
      }
      return true;
    };

    auto checkSquare = [&](int startRow, int startCol) -> bool {
      vector<int> freq(10, 0);
      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
          char num = board[startRow + i][startCol + j];
          if (num != '.') {
            if (++freq[num - '0'] > 1) {
              return false;
            }
          }
        }
      }
      return true;
    };

    for (int i = 0; i < n; i++) {
      if (!checkRow(board[i]))
        return false;
    }

    for (int i = 0; i < n; i++) {
      if (!checkCol(i))
        return false;
    }

    for (int i = 0; i < n; i += 3) {
      for (int j = 0; j < n; j += 3) {
        if (!checkSquare(i, j))
          return false;
      }
    }

    return true;
  }
};

int main() {
  vector<vector<char>> board1 = {{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                                 {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                                 {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                                 {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                                 {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                                 {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                                 {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                                 {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                                 {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

  vector<vector<char>> board2 = {{'8', '3', '.', '.', '7', '.', '.', '.', '.'},
                                 {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                                 {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                                 {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                                 {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                                 {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                                 {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                                 {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                                 {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

  Solution s;
  cout << "Board 1 is " << (s.isValidSudoku(board1) ? "valid" : "invalid")
       << endl;
  cout << "Board 2 is " << (s.isValidSudoku(board2) ? "valid" : "invalid")
       << endl;
}
