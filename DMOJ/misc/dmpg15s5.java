import java.util.*;
import java.io.*;
public class DMOJ {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static byte psa[][], grid[][];
    public static void main(String[] args) throws IOException{
        int N = readInt(), M = readInt(), cnt = 0; psa = new byte[N + 5][N + 5]; grid = new byte[N + 5][N + 5];
        for(int i = 0; i < M; i++){
            int a = readInt() + 1, b = readInt() + 1, c = readInt(), d = readInt();
            update(a, b, c, d);
        }
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= N; j++){
                psa[i][j] = (byte)(psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + grid[i][j]);
            }
        }
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= N; j++){
                if(psa[i][j] % 2 != 0){
                    cnt++;
                }
            }
        }
        out.println(cnt);
        out.close();
    }
    static void update (int a, int b, int c, int d) {
        grid[a][b]++;
        grid[a + c][b]--;
        grid[a][b + d]--;
        grid[a + c][b + d]++;
    }
    static String next () throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static long readLong () throws IOException {
        return Long.parseLong(next());
    }

    static int readInt () throws IOException {
        return Integer.parseInt(next());
    }

    static double readDouble () throws IOException {
        return Double.parseDouble(next());
    }

    static String readLine () throws IOException {
        return br.readLine().trim();
    }
}