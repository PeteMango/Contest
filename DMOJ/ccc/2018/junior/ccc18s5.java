import java.util.*;
import java.io.*;

public class ccc18s5 {
    public static class Edge implements Comparable<Edge> {
        int s, d;
        long wt;
        boolean v;
        public Edge(int s, int d, int wt, boolean v) {
            this.s = s;
            this.d = d;
            this.wt = wt;
            this.v = v;
        }
        @Override
        public int compareTo(Edge o) {
            return Long.compare(this.wt, o.wt);
        }
    }
    public static class DisjointSet {
        int par[], N;
        public DisjointSet(int N) {
            this.N = N;
            par = new int[N + 1];
            for (int i = 1; i <= N; i++) par[i] = i;
        }
        public int find(int x) {
            if (par[x] == x) {
                return x;
            }
            return par[x] = find(par[x]);
        }
        public void union(int x, int y) {
            par[x] = y;
        }
    }
    public static void main(String[] args) throws IOException {
        int N = readInt(), M = readInt(), P = readInt(), Q = readInt();
        long total = 0, MST = 0;
        PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
        for (int i = 1; i <= P; i++) pq.add(new Edge(readInt(), readInt(), readInt(), false));
        for (int i = 1; i <= Q; i++) pq.add(new Edge(readInt(), readInt(), readInt(), true));
        DisjointSet Ns = new DisjointSet(N), Ms = new DisjointSet(M);
        while (!pq.isEmpty()) {
            Edge e = pq.poll();
            if (!e.v) {
                total += e.wt * N;
                if (Ms.N != 0 && Ms.find(e.d) != Ms.find(e.s)) {
                    MST += Ns.N * e.wt;
                    Ms.union(Ms.find(e.d), Ms.find(e.s));
                    Ms.N -= 1;
                }
            } else {
                total += e.wt * M;
                if (Ns.N != 0 && Ns.find(e.d) != Ns.find(e.s)) {
                    MST += Ms.N * e.wt;
                    Ns.union(Ns.find(e.d), Ns.find(e.s));
                    Ns.N -= 1;
                }
            }
        }
        out.println(total - MST);
        exit();
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