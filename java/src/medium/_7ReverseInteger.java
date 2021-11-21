package medium;

/**
 * <a href="https://leetcode.com/problems/reverse-integer/">7. Reverse Integer</a>
 * */
public class _7ReverseInteger {

    public static void main(String[] args) {
        int res = new Solution().reverse(123);
        System.out.println(res); //321
    }

    static class Solution {
        public int reverse(int x) {
            int maxDiv10 = 214748364;
            int minDiv10 = -214748364;
            int res = 0;
            while (x != 0) {
                int num = x % 10;
                x = x / 10;
                if (res > maxDiv10 || res == maxDiv10 && num > 7) return 0;
                if (res < minDiv10 || res == minDiv10 && num < -8) return 0;
                res = 10 * res + num;
            }

            return res;
        }
    }
}



