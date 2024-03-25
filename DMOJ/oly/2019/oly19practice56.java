import java.util.*;
import java.io.*;
public class oly19practice56 {
    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        int M = scan.nextInt(), N = scan.nextInt(), U = scan.nextInt(), F = scan.nextInt(), D = scan.nextInt(), t = U + D, q = F + F;
        int cnt = 0, min = 0;
        scan.nextLine();
        String s = scan.nextLine();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'u' || c == 'd') {
                if (t + min <= M) {
                    cnt++;
                    min += t;
                } else break;
            } else if (c == 'f') {
                if (q + min <= M) {
                    cnt++;
                    min += q;
                } else break;
            }
        }
        System.out.println(cnt);
    }
}