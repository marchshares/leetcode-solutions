package com.lc.medium;

/**
 * <a href="https://leetcode.com/problems/longest-palindromic-substring/">5. Longest Palindromic Substring</a>
 * */
public class LongestPalindromicSubstring {

    public static void main(String[] args) {
        String res = new Solution().longestPalindrome("babad");
        System.out.println(res); //  "bab"
    }

    static class Solution {
        public String longestPalindrome(String s) {
            int n = s.length();

            for (int maxLen = n; maxLen > 0; maxLen--) {
                for (int i = 0; i < n - maxLen + 1; i++) {
                    if (isPalindrome2(s,i,i+maxLen)) {
                        return s.substring(i, i + maxLen);
                    }
                }
            }

            return "";
        }

        private boolean isPalindrome2(String s, int beginIndex, int endIndex) {
            int n = endIndex-beginIndex;

            for (int i = 0; i < n / 2; i++) {
                if (s.charAt(beginIndex+i) != s.charAt(beginIndex+n-1-i)) {
                    return false;
                }
            }

            return true;
        }
    }
}



