package easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * <a href="https://leetcode.com/problems/palindrome-number/">9. Palindrome Number</a>
 * */
public class _9PalindromeNumber {

    public static void main(String[] args) {
        boolean res = new Solution().isPalindrome(121);
        System.out.println(res);
    }

    static class Solution {
        public boolean isPalindrome(int x) {
            if (x < 0 || x % 10 == 0 && x != 0) {
                return false;
            }

            int rev = 0;
            while (x > rev) {
                rev = 10 * rev + x % 10;
                x = x / 10;
            }

            return x == rev || x == rev / 10;
        }

    }
}


