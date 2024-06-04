// Wed, May 29, 2024

import java.math.BigInteger;

class Solution {
    public int numSteps(String s) {
        BigInteger bigInt = new BigInteger(s, 2);
        BigInteger two = BigInteger.valueOf(2);
        BigInteger one = BigInteger.ONE;

        int ans = 0;
        while (bigInt.compareTo(one) > 0) {
            if (bigInt.mod(two).equals(BigInteger.ZERO)) {
                bigInt = bigInt.divide(two);
            } else {
                bigInt = bigInt.add(one);
            }
            ans += 1;
        }
        return ans;
    }
}
