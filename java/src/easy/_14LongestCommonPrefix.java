package easy;

/**
 * <a href="https://leetcode.com/problems/longest-common-prefix/">14. Longest Common Prefix</a>
 * */
public class _14LongestCommonPrefix {

    public static void main(String[] args) {
        String res = new Solution().longestCommonPrefix(new String[]{"flower", "flow", "flight"});
        System.out.println("fl".equals(res));
    }

    static class Solution {
        public String longestCommonPrefix(String[] strs) {
            if (strs.length == 0) {
                return "";
            }


            int len1 = strs[0].length();
            int pos = 0;

            while (pos < len1) {
                char c = strs[0].charAt(pos);
                int strNum = 0;
                while (strNum < strs.length && pos < strs[strNum].length()) {
                    if (c != strs[strNum].charAt(pos)) {
                        break;
                    }
                    strNum++;
                }

                if (strNum != strs.length) {
                    break;
                }

                pos++;
            }

            return strs[0].substring(0, pos);
        }
    }
}



