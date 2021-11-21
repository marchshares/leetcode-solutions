package medium;

/**
 * <a href="https://leetcode.com/problems/zigzag-conversion/">6. Zigzag Conversion</a>
 * */
public class _6ZigzagConversion {

    public static void main(String[] args) {
        String res = new Solution().convert("PAYPALISHIRING", 3);
        System.out.println(res); //"PAHNAPLSIIGYIR"
    }

    static class Solution {
        public String convert(String s, int numRows) {
            int len = s.length();
            if (numRows == 1 || len < numRows) return s;

            int step = 2 * numRows - 2;
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < numRows; i++) {

                for (int j = 0; j+i < len; j += step) {
                    sb.append(s.charAt(j+i));

                    if (i != 0 && i != numRows -1 && j+step-i < len) {
                        if (j+step-i == i+j) {
                            int h = 0;
                        }
                        sb.append(s.charAt(j+step-i));
                    }
                }
            }

            return sb.toString();
        }
    }
}



