#include <string>
using namespace std;

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
  vector<string> ans;
  string smallestFromLeaf(TreeNode *root) {
    ans.clear();
    traverse(root, "");
    for (string &str : ans) {
      reverse(str.begin(), str.end());
    }
    sort(ans.begin(), ans.end());
    return ans[0];
  }
  void traverse(TreeNode *node, string cur) {
    if (node == nullptr) {
      return;
    }

    cur += (char)(node->val + (int)('a'));

    if (isLeaf(node)) {
      ans.push_back(cur);
      return;
    }

    traverse(node->left, cur);
    traverse(node->right, cur);
  }

  bool isLeaf(TreeNode *node) {
    return node != nullptr && node->left == nullptr && node->right == nullptr;
  }
};
