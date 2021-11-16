package com.lc.easy;

/**
 * <a href="https://leetcode.com/problems/roman-to-integer/">13. Roman to Integer</a>
 * */
public class RomanToInteger {

    public static void main(String[] args) {
        int res = new Solution().romanToInt("III");
        System.out.println(res);
    }

    static class Solution {
        public int romanToInt(String s) {
            int num = 0;
            for (int i = 0; i < s.length(); i++) {
                char letter = s.charAt(i);

                if (letter == 'V') {
                    num += 5;
                    continue;
                }
                if (letter == 'L') {
                    num += 50;
                    continue;
                }
                if (letter == 'D') {
                    num += 500;
                    continue;
                }
                if (letter == 'M') {
                    num += 1000;
                    continue;
                }


                char nextLetter = i+1 < s.length() ? s.charAt(i+1) : 0;
                if (letter == 'I') {
                    if ((nextLetter == 'V' || nextLetter == 'X')) {
                        num -= 1;
                    } else {
                        num += 1;
                    }
                    continue;
                }
                if (letter == 'X'){
                    if ((nextLetter == 'L' || nextLetter == 'C')) {
                        num -= 10;
                    } else {
                        num += 10;
                    }
                    continue;
                }
                if (letter == 'C'){
                    if ((nextLetter == 'D' || nextLetter == 'M')) {
                        num -= 100;
                    } else {
                        num += 100;
                    }
                    continue;
                }
            }

            return num;
        }
    }
}



