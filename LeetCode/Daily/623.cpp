/* Tue, April 16, 2024 */

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  TreeNode *addOneRow(TreeNode *root, int val, int depth) {
    if (depth == 1) {
      TreeNode *newroot = new TreeNode(val, root, nullptr);
      return newroot;
    }
    addNode(root, val, depth - 1, 1);
    return root;
  }
  void addNode(TreeNode *root, int val, int desired_depth, int cur_depth) {
    if (root == nullptr) {
      return;
    }
    if (cur_depth == desired_depth) {
      TreeNode *leftreplace = new TreeNode(val, root->left, nullptr);
      root->left = leftreplace;

      TreeNode *rightreplace = new TreeNode(val, nullptr, root->right);
      root->right = rightreplace;
      return;
    }

    addNode(root->left, val, desired_depth, cur_depth + 1);
    addNode(root->right, val, desired_depth, cur_depth + 1);
  }
};

int main() {}
