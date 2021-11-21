package medium;

/**
 * <a href="https://leetcode.com/problems/container-with-most-water/">11. Container With Most Water</a>
 * */
public class _11ContainerWithMostWater {

    public static void main(String[] args) {
        int res = new Solution().maxArea(new int[]{1, 1});
        System.out.println(res == 1);
    }

    static class Solution {
        public int maxArea(int[] height) {
            int r = height.length - 1;
            int l = 0;

            int maxSq = 0;
            while (r > l) {
                int sq = (r-l) * Math.min(height[r], height[l]);
                maxSq = Math.max(maxSq, sq);

                if (height[r] < height[l]) {
                    int nextR = r-1;
                    while (height[r] >= height[nextR] && nextR > l) nextR--;

                    r = nextR;
                } else {
                    int nextL = l+1;
                    while (height[l] >= height[nextL] && nextL < r) nextL++;

                    l = nextL;
                }
            }

            return maxSq;
        }
    }
}



