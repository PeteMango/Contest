class Solution {

    public boolean satisfiesConditions(int[][] grid) {
        int n = grid.length, m = grid[0].length;

        for (int i = 0; i < m; i++) {
            int num = grid[0][i];
            for (int j = 0; j < n; j++) {
                if (grid[j][i] != num) {
                    return false;
                }
            }
        }
        for (int i = 0; i < m - 1; i++) {
            if (grid[0][i] == grid[0][i + 1]) {
                return false;
            }
        }
        return true;
    }
}
