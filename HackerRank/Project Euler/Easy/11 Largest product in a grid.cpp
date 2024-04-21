#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

vector<vector<int>> moves = { {1, 1}, {1, 0}, {1, -1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, 1}, {0, -1}};

int max(int a, int b) {
    return a > b ? a : b;
}

int up(vector<vector<int>> G, int x, int y) {
    if(y < 3) {
        return -1;
    }
    int ans = 1;
    for(int i = y-3; i <= y; i++) {
        ans *= G[x][i];
    }
    return ans;
}

int down(vector<vector<int>> G, int x, int y) {
    if(y > G.size() - 4) {
        return -1;
    }
    int ans = 1;
    for(int i = y; i <= y+3; i++) {
        ans *= G[x][i];
    }
    return ans;
}

int left(vector<vector<int>> G, int x, int y) {
    if(x < 3) {
        return -1;
    }
    int ans = 1;
    for(int i = x-3; i <= x; i++) {
        ans *= G[i][y];
    }
    return ans;
}

int right(vector<vector<int>> G, int x, int y) {
    if(x > G.size() - 4) {
        return -1;
    }
    int ans = 1;
    for(int i = x; i <= x+3; i++) {
        ans *= G[i][y];
    }
    return ans;
}

int diagonal_left(vector<vector<int>> G, int x, int y) {
    if(x < 3 || y < 3) {
        return -1;
    }
    int ans = 1;
    for(int i = 0; i <= 3; i++) {
        ans *= G[x - i][y - i];
    }
    return ans;
}

int diagonal_right(vector<vector<int>> G, int x, int y) {
    if(x < 3 || y > G[0].size() - 4) {
        return -1;
    }
    int ans = 1;
    for(int i = 0; i <= 3; i++) {
        ans *= G[x - i][y + i];
    }
    return ans;
}

int maxProduct(vector<vector<int>> G, int x, int y) {
    int up_prod = up(G, x, y);
    int down_prod = down(G, x, y);
    int left_prod = left(G, x, y);
    int right_prod = right(G, x, y);
    int diag_left_prod = diagonal_left(G, x, y);
    int diag_right_prod = diagonal_right(G, x, y);

    int max_dir_prod = max(up_prod, down_prod);
    max_dir_prod = max(max_dir_prod, left_prod);
    max_dir_prod = max(max_dir_prod, right_prod);
    max_dir_prod = max(max_dir_prod, diag_left_prod);
    max_dir_prod = max(max_dir_prod, diag_right_prod);

    return max_dir_prod;
}

int main()
{

    vector<vector<int>> grid(20);

    for (int i = 0; i < 20; i++) {
        grid[i].resize(20);

        string grid_row_temp_temp;
        getline(cin, grid_row_temp_temp);

        vector<string> grid_row_temp = split(rtrim(grid_row_temp_temp));

        for (int j = 0; j < 20; j++) {
            int grid_row_item = stoi(grid_row_temp[j]);

            grid[i][j] = grid_row_item;
        }
    }

    int max_ans = 0;
    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < 20; j++) {
            max_ans = max(max_ans, maxProduct(grid, i, j));
        }
    }

    cout << max_ans << "\n";

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
