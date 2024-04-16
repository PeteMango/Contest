#include <functional>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
  void test() {
    /*
    function<[return_type]([arg1 type], [arg2 type]...)[function_name] = [pass
    by reference/value]([arg1 name], [arg2 name]...) -> [return type] {

        return [return_variable]
    };
    */
    function<int(string, int)> functionDef = [&](string str, int num) -> int {
      return 0;
    };

    /*
    auto [function_name] = [pass by reference/value] ([arg1 name], [arg2
        name]...) -> [return type] {

        return [return_variable]
    };
    */
    auto autoDef = [&](string str, int num) -> int { return 0; };

    cout << functionDef("hello world", 1) << "\n";
    cout << autoDef("hello world", 1) << "\n";
  }
};

int main() {
  Solution s;
  s.test();
}
