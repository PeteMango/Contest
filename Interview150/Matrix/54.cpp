#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>> &matrix) {
    if (matrix.empty())
      return {};
    vector<int> spiral;
    int top = 0, bottom = matrix.size() - 1;
    int left = 0, right = matrix[0].size() - 1;

    while (top <= bottom && left <= right) {
      for (int j = left; j <= right; ++j)
        spiral.push_back(matrix[top][j]);
      top++;

      for (int i = top; i <= bottom; ++i)
        spiral.push_back(matrix[i][right]);
      right--;

      if (top <= bottom) {
        for (int j = right; j >= left; --j)
          spiral.push_back(matrix[bottom][j]);
        bottom--;
      }

      if (left <= right) {
        for (int i = bottom; i >= top; --i)
          spiral.push_back(matrix[i][left]);
        left++;
      }
    }
    return spiral;
  }
};

int main() {
  Solution s;
  vector<vector<int>> matrix1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  vector<int> ret = s.spiralOrder(matrix1);
  for (auto num : ret) {
    cout << num << " ";
  }
}
