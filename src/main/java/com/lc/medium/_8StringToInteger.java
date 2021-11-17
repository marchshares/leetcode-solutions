package com.lc.medium;

/**
 * <a href="https://leetcode.com/problems/string-to-integer-atoi/">8. String to Integer (atoi)</a>
 * */
public class _8StringToInteger {

    public static void main(String[] args) {
        int res = new Solution().myAtoi("42");
        System.out.println(res == 42);
    }

    static class Solution {
        public static final int MAX10 = Integer.MAX_VALUE / 10;
        public static final int MIN10 = Integer.MIN_VALUE / 10;

        public int myAtoi(String str) {
            if (str.isEmpty()) {
                return 0;
            }

            int i = 0;
            int n = str.length();

            char c = str.charAt(i++);
            while (c == ' ' && i < n) {
                c = str.charAt(i++);
            }

            int sign = 1;
            if (c == '+' || c == '-') {
                if (c == '-') {
                    sign = -1;
                }

                if (i >= n) {
                    return 0;
                }

                c = str.charAt(i++);
            }

            if (!isNum(c)) {
                return 0;
            }

            int res = 0;
            while (isNum(c) && i <= n) {
                int num = sign * char2number(c);

                if (res > MAX10 || res == MAX10 && num > 7) return Integer.MAX_VALUE;
                if (res < MIN10 || res == MIN10 && num < -8) return Integer.MIN_VALUE;
                res = 10 * res + num;

                if (i < n) {
                    c = str.charAt(i++);
                } else {
                    break;
                }
            }

            return res;
        }

        private boolean isNum(char c) {
            return c >= '0' && c <= '9';
        }

        private int char2number(char c) {
            return c - '0';
        }
    }
}



