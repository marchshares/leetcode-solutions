package com.lc.medium;

import java.util.HashMap;
import java.util.Map;

/**
 * <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">3. Longest Substring Without Repeating Characters</a>
 * */
public class LongestSubstringWithoutRepeatingCharacters {

    public static void main(String[] args) {
        int res = new Solution().lengthOfLongestSubstring("abcabcbb");
        System.out.println(res); //Output: 3
    }

    static class Solution {
        public int lengthOfLongestSubstring(String s) {
            Map<Character, Integer> map = new HashMap<>();

            int res = 0;
            for (int i = 0, j = 0; j < s.length(); j++) {

                if (map.containsKey(s.charAt(j))) {
                    i = Math.max(map.get(s.charAt(j))+1, i);
                }

                res = Math.max(res, j-i+1);
                map.put(s.charAt(j), j);
            }

            return res;
        }
    }
}



