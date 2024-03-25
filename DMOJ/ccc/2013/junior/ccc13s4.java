import java.util.*;
import java.io.*;
public class ccc13s4 {
    static ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
    static int N, M;
    public static void main(String[] args) throws IOException {
        N = readInt(); M = readInt();
        for(int i = 0; i <= N; i++) adj.add(new ArrayList<Integer>());
        for(int i = 0; i < M; i++) adj.get(readInt()).add(readInt());
        int start = readInt(), dest = readInt();
        boolean a2b = bfs(start, dest), b2a = bfs(dest, start);
        if (a2b) out.println("yes");
        else if(b2a) out.println("no");
        else out.println("unknown");
        exit();
    }
    static boolean bfs(int start, int dest){
        boolean vis[] = new boolean[N + 1];
        LinkedList<Integer> q = new LinkedList<Integer>();
        vis[start] = true;
        q.add(start);
        while(!q.isEmpty()){
            int cur = q.poll();
            for(int c: adj.get(cur)){
                if(!vis[c]){
                    vis[c] = true;
                    q.add(c);
                }
            }
        }
        if(vis[dest]) return true;
        return false;
    }
    final private static int BUFFER_SIZE = 1 << 16;
    private static DataInputStream din = new DataInputStream(System.in);
    private static byte[] buffer = new byte[BUFFER_SIZE];
    private static int bufferPointer = 0, bytesRead = 0;
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    public static String readLine() throws IOException {
        byte[] buf = new byte[2048]; // line length
        int cnt = 0, c;
        while ((c = Read()) != -1) {
            if (c == '\n')
                break;
            buf[cnt++] = (byte) c;
        }
        return new String(buf, 0, cnt);
    }
    public static String next() throws IOException {
        byte[] ret = new byte[2048];
        int idx = 0;
        byte c = Read();
        while (c <= ' ') {
            c = Read();
        }
        do {
            ret[idx++] = c;
            c = Read();
        } while (c != -1 && c != ' ' && c != '\n' && c != '\r');
        return new String(ret, 0, idx);
    }
    public static int readInt() throws IOException {
        int ret = 0;
        byte c = Read();
        while (c <= ' ')
            c = Read();
        boolean neg = (c == '-');
        if (neg)
            c = Read();
        do {
            ret = ret * 10 + c - '0';
        } while ((c = Read()) >= '0' && c <= '9');

        if (neg)
            return -ret;
        return ret;
    }
    public static long readLong() throws IOException {
        long ret = 0;
        byte c = Read();
        while (c <= ' ')
            c = Read();
        boolean neg = (c == '-');
        if (neg)
            c = Read();
        do {
            ret = ret * 10 + c - '0';
        } while ((c = Read()) >= '0' && c <= '9');
        if (neg)
            return -ret;
        return ret;
    }
    public static double readDouble() throws IOException {
        double ret = 0, div = 1;
        byte c = Read();
        while (c <= ' ')
            c = Read();
        boolean neg = (c == '-');
        if (neg)
            c = Read();

        do {
            ret = ret * 10 + c - '0';
        } while ((c = Read()) >= '0' && c <= '9');

        if (c == '.') {
            while ((c = Read()) >= '0' && c <= '9') {
                ret += (c - '0') / (div *= 10);
            }
        }

        if (neg)
            return -ret;
        return ret;
    }
    private static void fillBuffer() throws IOException {
        bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
        if (bytesRead == -1)
            buffer[0] = -1;
    }
    private static byte Read() throws IOException {
        if (bufferPointer == bytesRead)
            fillBuffer();
        return buffer[bufferPointer++];
    }
    public void close() throws IOException {
        if (din == null)
            return;
        din.close();
    }
    static void print(Object o) {
        out.print(o);
    }
    static void println(Object o) {
        out.println(o);
    }
    static void flush() {
        out.flush();
    }
    static void println() {
        out.println();
    }
    static void exit() throws IOException {
        din.close();
        out.close();
        System.exit(0);
    }
}